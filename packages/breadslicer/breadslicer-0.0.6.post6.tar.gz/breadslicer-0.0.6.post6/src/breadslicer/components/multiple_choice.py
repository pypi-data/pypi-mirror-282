from dataclasses import dataclass
from typing import Callable, Dict, List, Optional

import inquirer
from inquirer.questions import Question

from breadslicer.components.base import BaseComponent


@dataclass
class MultipleChoiceComponent(BaseComponent):
    default: List[str] | None | Callable[[Dict[str, str | bool]], List[str]]
    choices: List[str]
    ignore: Optional[Callable[[Dict[str, str | bool]], bool]] = None

    def component_question(self) -> Question:
        return inquirer.Checkbox(
            name=self.name,
            message=self.message,
            choices=self.choices,
            default=self.default,  # type: ignore
            ignore=self.ignore,  # type: ignore
        )
