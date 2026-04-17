from typing import Dict, Any

from backend.db.repositories.user_repository import UserRepository
from backend.web.service.type_errors import ValidationResult, TypeUserError


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
