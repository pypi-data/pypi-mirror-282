#!/usr/bin/env python3
import fcntl
import io
import os
import pathlib
import shlex
import subprocess
import sys
import threading
from typing import IO, Any, Literal, Union, cast

import click
import packaging.utils
import pydantic
import toml

data_folder = pathlib.Path(__file__).parent.joinpath("data")


def set_non_blocking(buffer: IO[str]):
    """
    Sets non-blocking reads for the underlying file handle for a buffer
    """
    fileno = buffer.fileno()
    fl = fcntl.fcntl(fileno, fcntl.F_GETFL)
    fcntl.fcntl(fileno, fcntl.F_SETFL, fl | os.O_NONBLOCK)


def reader(process_complete: threading.Event, in_buffer: IO[str], out_buffer: IO[str]):
    """
    Logs data from a stdout/stderr buffer (e.g., stdout=subprocess.PIPE) to stderr.

    Returns a callable for easier use with `threading.Thread`.
    """

    def inner():
        # helper method to log from a buffer
        def read():
            data = in_buffer.read(20)
            if data is None:
                return
            sys.stderr.write(data)
            out_buffer.write(data)

        while not process_complete.is_set():
            # read until process is complete
            read()
        # perform final read
        read()

    return inner


def run_cmd(cmd: list[str], **kwargs):
    """
    Helper method that runs a command.

    Accepts the same kwargs as `subprocess.Popen`.
    """
    # log command
    cmd_str = f"{shlex.join(cmd)}"
    if env := kwargs.get("env"):
        # if 'env' is defined, only log env overrides
        diff = {}
        for key, value in env.items():
            if os.environ.get(key) == value:
                continue
            diff[key] = value
        diff_str = " ".join(f"{k}={v}" for k, v in diff.items())
        if diff_str:
            cmd_str += f" (env: {diff_str})"
    if cwd := kwargs.get("cwd"):
        # if 'cwd' is defined, log cwd
        cmd_str += f" (cwd: {cwd})"
    click.echo(f"$ {cmd_str}", err=True)

    # create popen
    kwargs["encoding"] = "utf-8"
    kwargs["stdout"] = subprocess.PIPE
    kwargs["stderr"] = subprocess.PIPE
    popen = subprocess.Popen(cmd, **kwargs)

    # create readers
    is_complete = threading.Event()
    in_stdout = cast(IO[str], popen.stdout)
    in_stderr = cast(IO[str], popen.stderr)
    set_non_blocking(in_stdout)
    set_non_blocking(in_stderr)
    out_stdout = io.StringIO()
    out_stderr = io.StringIO()
    readers = [
        threading.Thread(target=reader(is_complete, in_stdout, out_stdout)),
        threading.Thread(target=reader(is_complete, in_stderr, out_stderr)),
    ]

    # start readers
    [r.start() for r in readers]

    # wait for command to complete
    popen.wait()
    is_complete.set()

    # wait for readers to terminate
    [r.join() for r in readers]

    out_stdout.seek(0)
    stdout = out_stdout.read()

    if popen.returncode != 0:
        # command failed
        out_stderr.seek(0)
        stderr = out_stderr.read()
        raise subprocess.CalledProcessError(
            cmd=shlex.join(cmd),
            output=stdout,
            returncode=popen.returncode,
            stderr=stderr,
        )

    return stdout


def validator(type: Any):
    """
    Uses pydantic to create a validator for an arbitrary type.

    Intended to be used with the `type` kwarg to click.argument/option.
    """

    def inner(value: str):
        return pydantic.TypeAdapter(type).validate_python(value)

    return inner


def get_package_data() -> dict:
    """
    Parses a python package's pyproject.toml and retuns the parsed data as a `dict`.
    """
    pyproject_toml = pathlib.Path.cwd().joinpath("pyproject.toml")
    if not pyproject_toml.exists():
        raise FileNotFoundError(pyproject_toml)
    return toml.loads(pyproject_toml.read_text())


def find_python_build_files() -> list[pathlib.Path]:
    """
    Finds python build files that match the current project name and version.
    """
    package = get_package_data()
    name = package["project"]["name"]
    version = package["project"]["version"]

    pkg_name = packaging.utils.canonicalize_name(name).replace("-", "_")
    pkg_version = packaging.utils.canonicalize_version(
        version, strip_trailing_zero=False
    )
    dist_folder = pathlib.Path.cwd().joinpath(f"dist")
    files = []
    prefix = f"{pkg_name}-{pkg_version}"
    for file in dist_folder.iterdir():
        if file.name == f"{prefix}.tar.gz":
            # <name>-<version>.tar.gz
            files.append(file)
        if file.name.startswith(f"{prefix}-py"):
            # <name>-<version>-py3-none-any.whl
            files.append(file)
    return files


def run_docker_build(push: bool = False):
    """
    This method wraps `docker buildx build`.

    NOTE: Both build and publish use this method
    """
    # determine the image tag
    package = get_package_data()
    name = package["project"]["name"]
    version = package["project"]["version"].replace("+", "-")
    tag = f"docker.io/benfiola/{name}:{version}"

    # build the image
    cmd = [
        "docker",
        "buildx",
        "build",
        "--platform=linux/arm64,linux/amd64",
        f"--tag={tag}",
    ]
    if push:
        cmd.extend(["--push"])
    cmd.extend(["."])

    return run_cmd(cmd)


def main():
    try:
        grp_main()
    except Exception as e:
        click.echo(f"error: {e}", err=True)
        sys.exit(1)


@click.group()
def grp_main():
    pass


Flavor = Union[Literal["python"], Literal["docker"]]


@grp_main.command("build")
@click.argument("flavor", type=validator(Flavor))
def cmd_build(flavor: Flavor):
    if flavor == "python":
        run_cmd(["python", "-m", "build"])
        if len(find_python_build_files()) == 0:
            raise RuntimeError(f"no built files found")
    elif flavor == "docker":
        run_docker_build(push=False)


@grp_main.command("format")
@click.argument("files", type=pathlib.Path, nargs=-1)
def cmd_format(files: list[str]):
    file_strs = list(map(str, files))
    isort_config = data_folder.joinpath("isort.toml")
    run_cmd(["isort", f"--settings={isort_config}", *file_strs])
    black_config = data_folder.joinpath("black.toml")
    run_cmd(["black", f"--config={black_config}", *file_strs])


@grp_main.command("print-next-version")
@click.option("--as-tag", is_flag=True)
def cmd_print_next_version(*, as_tag: bool = False):
    command = ["python", "-m", "semantic_release", "--noop", "--strict", "version"]
    if as_tag is True:
        command.extend(["--print-tag"])
    else:
        command.extend(["--print"])
    env = {"GH_TOKEN": "undefined", **os.environ}
    version = run_cmd(command, env=env).strip()
    click.echo(version)


@grp_main.command("publish")
@click.argument("flavor", type=validator(Flavor))
@click.option("--token")
def cmd_publish(*, flavor: Flavor, token: str):
    if flavor == "docker":
        run_cmd(["docker", "login", "--username=benfiola", f"--password={token}"])
        run_docker_build(push=True)
    else:
        # validate expected build files exist
        files = find_python_build_files()
        if len(files) == 0:
            raise RuntimeError(f"no built files found")

        run_cmd(
            [
                "python",
                "-m",
                "twine",
                "--no-color",
                "upload",
                "--disable-progress-bar",
                "--repository-url=https://upload.pypi.org/legacy/",
                "-u=__token__",
                f"-p={token}",
                *list(map(str, files)),
            ]
        )


@grp_main.command("set-version")
@click.argument("version")
def cmd_set_version(*, version: str):
    package = get_package_data()
    package["project"]["version"] = version
    pyproject_file = pathlib.Path.cwd().joinpath("pyproject.toml")
    pyproject_file.write_text(toml.dumps(package))


if __name__ == "__main__":
    main()
