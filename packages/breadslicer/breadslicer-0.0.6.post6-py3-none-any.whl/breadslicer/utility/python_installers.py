from abc import abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from breadslicer.utility.abstractdataclass import AbstractDataclass
from breadslicer.utility.command import capture_cmd, cmd


@dataclass
class PythonInstaller(AbstractDataclass):
    python_version: str

    @abstractmethod
    def create_venv(self) -> None: ...

    @abstractmethod
    def is_ready(self) -> bool: ...


@dataclass
class PyEnvSimpleInstaller(PythonInstaller):
    python_version: str
    pyenv_bin: Optional[Path] = None
    pyenv_python_bin: Optional[Path] = None

    def __post_init__(self):
        """post_init

        If the `poetry_bin` parameter was not set in initialization
        it will be found by running `which poetry` shell command.
        """
        try:
            self.pyenv_bin = (
                Path(capture_cmd(["which", "pyenv"]).replace("\n", ""))
                if self.pyenv_bin is None
                else self.pyenv_bin
            )
        except Exception:
            print("Could not locate pyenv will use system python")
            return

        pyenv = capture_cmd(["pyenv", "root"]).replace("\n", "")
        self.pyenv_python_bin = (
            Path(pyenv) / "versions" / self.python_version / "bin" / "python"
        )

    def pyenv(self) -> Path:
        pyenv = capture_cmd(["pyenv", "root"]).replace("\n", "")
        path = Path(pyenv) / "versions" / self.python_version / "bin" / "python"
        assert path.exists()
        return path

    def create_venv(self) -> None:
        cmd([str(self.pyenv_python_bin), "-m", "venv", ".venv"])

    def is_ready(self) -> bool:
        return (
            self.pyenv_bin is not None
            and self.pyenv_python_bin is not None
            and self.pyenv_bin.exists()
            and self.pyenv_python_bin.exists()
        )
