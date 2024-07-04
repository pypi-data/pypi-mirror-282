import subprocess
from pathlib import Path
from typing import Dict, List, Optional


def cmd(
    commands: List[str],
    cwd: Optional[Path] = None,
    env: Optional[Dict[str, str]] = None,
) -> None:
    print(" ".join(commands))
    subprocess.run(
        commands, capture_output=False, check=True, shell=False, cwd=cwd, env=env
    )


def shell(
    commands: List[str],
    cwd: Optional[Path] = None,
    env: Optional[Dict[str, str]] = None,
) -> str:
    cmd_str = " ".join(commands)
    print(cmd_str)
    rc: subprocess.CompletedProcess[bytes] = subprocess.run(
        cmd_str, capture_output=True, check=False, shell=True, cwd=cwd, env=env
    )
    if rc.returncode == 0:
        return rc.stdout.decode("utf-8")
    else:
        raise RuntimeError(
            f"ERROR running command {' '.join(commands)}:\n {rc.stderr!r} \n"
            f"{rc.stdout!r}"
        )


def capture_cmd(commands: List[str], cwd: Optional[Path] = None) -> str:
    print(" ".join(commands))
    rc: subprocess.CompletedProcess[bytes] = subprocess.run(
        commands, capture_output=True, check=True, cwd=cwd
    )
    if rc.returncode == 0:
        return rc.stdout.decode("utf-8")
    else:
        raise RuntimeError(
            f"ERROR running command {' '.join(commands)}:\n {rc.stderr!r}"
        )


def poetry_run(commands: List[str], cwd: Optional[Path] = None) -> None:
    shell(
        ["poetry", "run"] + commands,
        cwd,
        env={
            "POETRY_VIRTUALENVS_IN_PROJECT": "true",
            "POETRY_VIRTUALENVS_CREATE": "false",
        },
    )
