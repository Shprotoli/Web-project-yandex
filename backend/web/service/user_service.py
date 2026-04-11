from enum import Enum
from typing import List, Dict, Any

from backend.db.repositories.user_repository import UserRepository


class TypeUserError(Enum):
    PASSWORD = "password"
    USERNAME = "username"
    EMAIL = "email"
    OTHER = "other"


class ValidationResult:
    def __init__(self):
        self._errors: List[Dict[str, str]] = []

    def add_error(self, type: TypeUserError, message: str) -> None:
        self._errors.append({
            "type": type.value,
            "message": message,
        })

    def is_valid(self) -> bool:
        return len(self._errors) == 0

    def get_errors(self) -> List[Dict[str, str]]:
        return self._errors


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def validate_registration(self, data: Dict[str, Any]) -> ValidationResult:
        result = ValidationResult()

        password = data.get("password")
        confirm = data.get("confirm_password")
        email = data.get("email")
        username = data.get("username")

        if not password:
            result.add_error(TypeUserError.PASSWORD, "Пароль обязателен")
        elif len(password) < 8:
            result.add_error(TypeUserError.PASSWORD, "Пароль должен быть не менее 8 символов")

        if password and password != confirm:
            result.add_error(TypeUserError.PASSWORD, "Пароли не совпадают")

        if email and self.user_repository.get_by_email(email):
            result.add_error(TypeUserError.EMAIL, "Email уже используется")

        if username and self.user_repository.get_by_username(username):
            result.add_error(TypeUserError.USERNAME, "Username уже занят")

        return result
