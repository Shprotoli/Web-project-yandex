from backend.other.extensions import db
from backend.db.models.blitz import Blitz


class BlitzRepository:
    @staticmethod
    def get_all() -> list[Blitz]:
        return Blitz.query.order_by(Blitz.id.asc()).all()

    @staticmethod
    def get_by_title(title: str) -> Blitz | None:
        return Blitz.query.filter_by(title=title).first()

    @staticmethod
    def get_by_id(blitz_id: int) -> Blitz | None:
        return db.session.get(Blitz, blitz_id)

    @staticmethod
    def get_by_id_subject(id_subject: str) -> Blitz | None:
        return Blitz.query.filter_by(id_subject=id_subject).all()

    @staticmethod
    def create(blitz: Blitz) -> Blitz:
        db.session.add(blitz)
        db.session.commit()
        return blitz

    @staticmethod
    def update() -> None:
        db.session.commit()

    @staticmethod
    def delete(blitz: Blitz) -> None:
        db.session.delete(blitz)
        db.session.commit()
