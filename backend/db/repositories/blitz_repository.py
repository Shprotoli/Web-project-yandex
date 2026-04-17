from backend.other.extensions import db
from backend.db.models.blitz import Blitz


class BlitzRepository:
    def get_by_title(self, title: str) -> Blitz | None:
        return Blitz.query.filter_by(title=title).first()

    def get_by_id(self, user_id: int) -> Blitz | None:
        return Blitz.query.get(user_id)

    def create(self, user: Blitz) -> Blitz:
        db.session.add(user)
        db.session.commit()
        return user
