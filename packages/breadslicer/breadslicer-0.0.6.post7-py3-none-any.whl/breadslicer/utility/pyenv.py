import re
from typing import List

from breadslicer.utility.command import capture_cmd, cmd

VERSION_PATTERN = re.compile(r"^([^\d]*\d+.\d+)\.?\d*.*$")


class PyEnv:

    def __init__(self) -> None:
        cmd(["which", "pyenv"])

    def versions(self) -> List[str]:
        output = capture_cmd(["pyenv", "versions"])
        vs = [
            version.strip()
            for version in output.split("\n")
            if "system" not in version and not version == ""
        ]
        return vs

    def versions_short(self) -> List[str]:
        return sorted(
            list({VERSION_PATTERN.sub(r"\1", v) for v in self.versions()})
        )  # Returns the sorted short version of unique python versions installed
