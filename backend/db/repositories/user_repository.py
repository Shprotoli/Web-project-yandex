from backend.other.extensions import db
from backend.db.models.user import User


class UserRepository:
    def get_by_email(self, email: str) -> User | None:
        return User.query.filter_by(email=email).first()

    def get_by_id(self, user_id: int) -> User | None:
        return User.query.get(user_id)

    def create(self, user: User) -> User:
        db.session.add(user)
        db.session.commit()
        return user
