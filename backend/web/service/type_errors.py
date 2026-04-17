from typing import List, Dict
from enum import Enum


class TypeError:
    """
    Абстрактный класс типов ошибок в бизнес логике (*_service)
    """
    OTHER = "other"

    def value(self):
        pass


class TypeUserError(TypeError, Enum):
    PASSWORD = "password"
    USERNAME = "username"
    EMAIL = "email"


class ValidationResult:
    def __init__(self):
        self._errors: List[Dict[str, str]] = []

    def add_error(self, type: TypeError, message: str) -> None:
        self._errors.append({
            "type": type.value,
            "message": message,
        })

    def is_valid(self) -> bool:
        return len(self._errors) == 0

    def get_errors(self) -> List[Dict[str, str]]:
        return self._errors
