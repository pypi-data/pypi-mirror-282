from typing import Dict, List, Tuple

from breadslicer.components.base import BaseComponent
from breadslicer.components.choice import ChoiceComponent
from breadslicer.components.confirm import ConfirmComponent
from breadslicer.components.editor import EditorComponent
from breadslicer.components.multiple_choice import MultipleChoiceComponent
from breadslicer.components.text import AuthorComponent, EmailComponent, TextComponent
from breadslicer.utility.pyenv import VERSION_PATTERN, PyEnv


class Q:
    @staticmethod
    def is_service(answers: Dict[str, str | bool]) -> bool:
        """Utility function to determine if the project type
        is a service.
        """
        none_service_types = {"app", "lib"}
        return (
            answers["project_type"] not in none_service_types
            if "project_type" in answers
            else False
        )

    @staticmethod
    def is_not_service(answers: Dict[str, str | bool]) -> bool:
        """Utility function to determine if the project type
        is a not service.
        """
        none_service_types = {"app", "lib"}
        return (
            answers["project_type"] in none_service_types
            if "project_type" in answers
            else False
        )

    @staticmethod
    def is_gitlab(answers: Dict[str, str | bool]) -> bool:
        """Utility function to determine if the project type
        is a not service.
        """
        return answers["ci_system"] == "gitlab" if "ci_system" in answers else False

    @staticmethod
    def python_version(answers: Dict[str, str | bool]) -> List[str]:
        """Utility function to determine if the project type
        is a not service.
        """
        assert not isinstance(answers["python_version"], bool)
        return [answers["python_version"]]

    @staticmethod
    def python_short(answers: Dict[str, str | bool]) -> List[str]:
        """Utility function to determine if the project type
        is a not service.
        """
        assert not isinstance(answers["python_version"], bool)
        return [VERSION_PATTERN.sub(r"\1", answers["python_version"])]

    @classmethod
    def project_layout(cls) -> BaseComponent:
        layouts: List[Tuple[str, str]] = [
            ("Flat layout", "flat"),
            ("Source layout", "src"),
        ]
        return ChoiceComponent(
            name="project_layout",
            message="[Project] Choose the project layout",
            default=None,
            choices=layouts,
            ignore=cls.is_service,
        )

    @classmethod
    def build_system(cls) -> BaseComponent:
        systems: List[Tuple[str, str]] = [
            ("Poetry", "poetry"),
            ("Rye", "rye"),
            ("Setuptools", "setuptools"),
        ]
        return ChoiceComponent(
            name="build_system",
            message="[Build] Select build system",
            default=None,
            choices=systems,
            ignore=cls.is_not_service,
        )

    @staticmethod
    def git_hooks() -> BaseComponent:
        return ConfirmComponent(
            name="use_commit_hooks",
            message="[GIT] Do you want to use git commit hooks "
            "to run verify before commits?",
            default=True,
        )

    @staticmethod
    def ci_system() -> BaseComponent:
        systems: List[Tuple[str, str]] = [
            ("Gitlab", "gitlab"),
            ("No CI system", "none"),
        ]
        return ChoiceComponent(
            name="ci_system",
            message="[CI] What CI system should be used?",
            default="gitlab",
            choices=systems,
            ignore=None,
        )

    @classmethod
    def gitlab_system(cls) -> BaseComponent:
        systems: List[str] = [
            "Gitlab",
            "No CI system",
        ]
        return MultipleChoiceComponent(
            name="ci_system",
            message="[CI] What CI system should be used?",
            default=[],
            choices=systems,
            ignore=cls.is_gitlab,
        )

    @staticmethod
    def docker_base() -> BaseComponent:
        docker_images: List[Tuple[str, str]] = [
            ("alpine", "alpine"),
            ("debian", "debian"),
            ("debian-slim", "slim"),
        ]
        return ChoiceComponent(
            name="docker_base",
            message="[Docker] Select base python docker image from dockerhub",
            default="debian",
            choices=docker_images,
            ignore=None,
        )

    @classmethod
    def select_python_test_versions(cls) -> BaseComponent:
        pyenv = PyEnv()
        return MultipleChoiceComponent(
            name="python_test_versions",
            message="[Python] Select python version",
            choices=[version for version in pyenv.versions_short()],
            default=cls.python_short,
            ignore=cls.is_service,
        )

    @classmethod
    def select_python_version(cls) -> BaseComponent:
        pyenv = PyEnv()
        return ChoiceComponent(
            name="python_version",
            message="[Python] Select python version",
            choices=[(version, version) for version in pyenv.versions()],
            default=None,
            ignore=None,
        )

    @classmethod
    def features(cls) -> List[BaseComponent]:

        return []

    @staticmethod
    def project_info() -> List[BaseComponent]:

        project_name = TextComponent(
            name="project_name",
            message="[Project] Project name",
            default="",
        )
        project_slug = TextComponent(
            name="project_slug",
            message="[Project] Project slug",
            default=lambda answers: answers["project_name"]
            .lower()
            .replace(" ", "_")
            .replace("-", "_"),
        )
        project_author_name = AuthorComponent(
            name="project_author_name",
            message="[Project] Type in name of the author",
        )
        project_author_email = EmailComponent(
            name="project_author_email", message="[Project] Type in email of author"
        )
        project_short_description = EditorComponent(
            name="project_short_description",
            message="[Project] Type in short project description",
        )

        return [
            project_name,
            project_slug,
            project_author_name,
            project_author_email,
            project_short_description,
        ]
