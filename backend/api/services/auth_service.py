from typing import Tuple, List

from datetime import UTC, datetime, timedelta
from secrets import token_urlsafe

from backend.db.models.user import User
from backend.db.repositories.session_repository import SessionRepository
from backend.db.repositories.user_repository import UserRepository
from backend.web.service.hasher import BcryptPasswordHasher
from backend.web.service.user_service import UserService


class AuthService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.session_repository = SessionRepository()
        self.user_service = UserService(self.user_repository)
        self.password_hasher = BcryptPasswordHasher()

    def register(self, data: dict) -> Tuple[User | None, List[dict]]:
        validation_result = self.user_service.validate_registration(data)
        if not data.get("email"):
            validation_result.add_error(type=type("EmailType", (), {"value": "email"})(), message="Email обязателен")
        if not data.get("username"):
            validation_result.add_error(type=type("UsernameType", (), {"value": "username"})(), message="Username обязателен")

        if not validation_result.is_valid():
            return None, validation_result.get_errors()

        user = User(
            username=data["username"],
            email=data["email"],
            password=self.password_hasher.hash(data["password"]),
        )
        self.user_repository.create(user)
        return user, []

    def login(self, username: str, password: str, session_ttl_hours: int = 24):
        user = self.user_repository.get_by_username(username)
        if user is None:
            return None, None

        if not self.password_hasher.verify(password, user.password):
            return None, None

        expires_at = datetime.now(UTC) + timedelta(hours=session_ttl_hours)
        session = self.session_repository.create(
            user_id=user.id,
            token=token_urlsafe(32),
            expires_at=expires_at,
        )
        return user, session

    def get_current_user_by_token(self, token: str):
        session = self.session_repository.get_active_by_token(token)
        if session is None:
            return None, None
        return session.user, session
