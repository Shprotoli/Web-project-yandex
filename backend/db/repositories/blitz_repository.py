from backend.other.extensions import db
from backend.db.models.blitz import Blitz


class BlitzRepository:
    @staticmethod
    def get_by_title(title: str) -> Blitz | None:
        return Blitz.query.filter_by(title=title).first()

    @staticmethod
    def get_by_id(user_id: int) -> Blitz | None:
        return Blitz.query.get(user_id)

    @staticmethod
    def create(user: Blitz) -> Blitz:
        db.session.add(user)
        db.session.commit()
        return user
