from dataclasses import dataclass
from pathlib import Path
from typing import Dict

from breadslicer.utility.command import cmd
from breadslicer.utility.fs import remove_paths, rename_path
from breadslicer.utility.installers import Installer


@dataclass
class Finalize:
    answers: Dict[str, str]
    installer: Installer

    def docs(self):
        """Create new docs project"""
        project_name = self.answers["project_name"]
        project_author_name = self.answers["project_author_name"]
        self.installer.run(
            [
                "sphinx-quickstart",
                "--sep",
                "--release=v0.0.0",
                f"--project={ project_name }",
                f"--author='{ project_author_name }'",
                "--language=en",
                "docs",
            ]
        )
        rename_path(
            Path("doc_conf") / Path("conf.py"), Path("docs/source") / Path("conf.py")
        )
        remove_paths([Path("doc_conf/")])

    def pre_commit_hooks(self):
        install_commit_hooks = self.answers["use_commit_hooks"]
        if install_commit_hooks:
            cmd(["git", "init"])
            self.installer.run(["pre-commit", "install"])
        else:
            remove_paths([Path(".pre-commit-config.yaml")])

    def ci_install(self):
        ci_system = self.answers["ci_system"]
        if ci_system == "gitlab":
            remove_paths([Path(".github")])
        elif ci_system == "github":
            remove_paths([Path(".gitlab/"), Path(".gitlab-ci.yml")])
        else:
            raise RuntimeError(
                f"If statements not exhaustive, expected gitlab/github, got {ci_system}"
            )

    def remove_main(self):
        project_slug = self.answers["project_slug"]
        remove_paths(
            [
                Path(f"src/{project_slug}/main.py"),
                Path(f"{project_slug}/main.py"),
                Path("run.sh"),
            ]
        )

    def app(self):
        layout = self.answers["project_layout"]
        if layout == "flat":
            self.flat()
        elif layout == "src":
            self.src()

    def lib(self):
        layout = self.answers["project_layout"]
        if layout == "flat":
            self.flat()
        elif layout == "src":
            self.src()

    def django(self):
        """Install django packages and remove unused directory"""

        project_slug = self.answers["project_slug"]
        remove_paths([Path("flask"), Path("flat"), Path("src")])

        self.installer.run(
            [
                "django-admin",
                "startproject",
                "--template",
                "django/project_template/",
                f"{project_slug}",
                ".",
            ]
        )
        remove_paths([Path("django")])

    def flask(self):
        """Remove everything not related to flask and install python packages
        related to flask"""

        remove_paths([Path("django"), Path("flat"), Path("src")])

    def flat(self):
        project_slug = self.answers["project_slug"]
        remove_paths(
            [
                Path("django"),
                Path("flask"),
                Path("src"),
                Path("templates"),
            ]
        )
        rename_path(Path("flat"), Path(project_slug))

    def src(self):
        print("expected to remove some directories")
        remove_paths([Path("django"), Path("flask"), Path("flat")])
