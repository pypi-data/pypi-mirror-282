from pathlib import Path
from typing import Any, Dict, List, Tuple

from breadslicer.application.slice import BreadSlice
from breadslicer.components.base import BaseComponent
from breadslicer.components.choice import ChoiceComponent
from breadslicer.utility.package_installers import PoetryEnvPackageInstaller
from breadslicer.utility.python_installers import PyEnvSimpleInstaller
from opinionated.cleanup import Finalize
from opinionated.dependencies import Dependencies
from opinionated.project_types import ProjectTypes
from opinionated.questions import Q


class OpinionatedBreadSlice(BreadSlice):
    includes_path: Path = Path(__file__).parent / "includes"
    templates_path: Path = Path(__file__).parent / "templates"
    excludes: List[str] = [
        "__pycache__/*"
    ]  # List of paths that should be excluded from the template folder when rendering

    """This is the opinionated breadslicer python project template"""

    @property
    def description(self) -> str:
        return (
            "This is the opinionated project template, "
            "choose project type, together with ci configurations."
        )

    @staticmethod
    def project_types() -> BaseComponent:
        p_types: List[Tuple[str, str]] = [
            ("Command-line application", ProjectTypes.app.value),
            ("Library", ProjectTypes.lib.value),
            ("Django application", ProjectTypes.django.value),
            ("Flask application", ProjectTypes.flask.value),
        ]
        return ChoiceComponent(
            name="project_type",
            message="[Project] What type of project is this?",
            default=None,
            choices=p_types,
            ignore=None,
        )

    def questions(self) -> List[BaseComponent]:
        """`questions` method of the `Bread` will implement the form
        to be entered by the user.
        """
        q: List[BaseComponent] = [
            *Q.project_info(),
            Q.select_python_version(),
            self.project_types(),
            Q.project_layout(),
            Q.select_python_test_versions(),
            Q.git_hooks(),
            Q.ci_system(),
            Q.docker_base(),
        ]
        return q

    def pre_render(self, answers: Dict[Any, Any], directory: Path) -> Dict[Any, Any]:
        return answers

    def post_render(self, answers: Dict[Any, Any], directory: Path) -> None:
        python_installer = PyEnvSimpleInstaller(answers["python_version"])
        if python_installer.is_ready():
            python_installer.create_venv()
        package_installer = PoetryEnvPackageInstaller(
            directory=directory,
        )

        deps = Dependencies(installer=package_installer, answers=answers)
        finalize = Finalize(answers=answers, installer=package_installer)

        # Install dependencies based on project type
        # Clean up afterwards
        match ProjectTypes[answers["project_type"]]:
            case ProjectTypes.app:
                deps.app()
                finalize.app()
            case ProjectTypes.lib:
                deps.lib()
                finalize.remove_main()
                finalize.lib()
            case ProjectTypes.django:
                deps.django()
                finalize.remove_main()
                finalize.django()
            case ProjectTypes.flask:
                deps.flask()
                finalize.flask()

        finalize.docs()
        finalize.ci_install()
        finalize.pre_commit_hooks()
