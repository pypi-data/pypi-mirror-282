from typing import List

from breadslicer.utility.command import capture_cmd, cmd


class PyEnv:

    def __init__(self) -> None:
        cmd(["which", "pyenv"])

    def versions(self) -> List[str]:
        output = capture_cmd(["pyenv", "versions"])
        return [
            version.strip()
            for version in output.split("\n")
            if "system" not in version and not version == ""
        ]
