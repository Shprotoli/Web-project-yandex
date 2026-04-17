from backend.other.extensions import db
from backend.db.models.user import User


class UserRepository:
    @staticmethod
    def get_by_email(email: str) -> User | None:
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_by_username(username: str) -> User | None:
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_by_id(user_id: int) -> User | None:
        return User.query.get(user_id)

    @staticmethod
    def create(user: User) -> User:
        db.session.add(user)
        db.session.commit()
        return user
