import os
from abc import abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

from breadslicer.utility.abstractdataclass import AbstractDataclass
from breadslicer.utility.command import capture_cmd, shell


@dataclass
class PackageInstaller(AbstractDataclass):
    directory: Path

    @abstractmethod
    def run(self, command: List[str]) -> str: ...

    @abstractmethod
    def install_package(self, package: str, group: Optional[str] = None) -> None: ...

    @abstractmethod
    def install_packages(
        self, packages: List[str], group: Optional[str] = None
    ) -> None: ...


@dataclass
class PoetryEnvPackageInstaller(PackageInstaller):
    directory: Path
    poetry_bin: Optional[Path] = None

    def __post_init__(self):
        """post_init

        If the `poetry_bin` parameter was not set in initialization
        it will be found by running `which poetry` shell command.
        """
        self.poetry_bin = (
            Path(capture_cmd(["which", "poetry"]).replace("\n", ""))
            if self.poetry_bin is None
            else self.poetry_bin
        )
        assert self.poetry_bin.exists()

    def _exec(self, command: List[str]) -> str:
        env = os.environ.copy()
        return shell(
            [str(self.poetry_bin), *command],
            cwd=self.directory,
            env={
                "PATH": env["PATH"],
                "POETRY_VIRTUALENVS_IN_PROJECT": "true",
                "POETRY_VIRTUALENVS_CREATE": "false",
            },
        )

    def run(self, command: List[str]) -> str:
        return self._exec(["run", *command])

    def poetry_install(
        self, package: str, group: Optional[str] = None, cwd: Optional[Path] = None
    ) -> None:
        if group:
            self._exec(
                ["add", package, f"--group={group}"],
            )
        else:
            self._exec(
                ["add", package],
            )

    def install_package(self, package: str, group: Optional[str] = None) -> None:
        self.poetry_install(package, group, self.directory)

    def install_packages(
        self, packages: List[str], group: Optional[str] = None
    ) -> None:
        for package in packages:
            self.install_package(package, group=group)
