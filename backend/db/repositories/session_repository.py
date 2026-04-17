from datetime import datetime

from backend.db.models.session import Session
from backend.other.extensions import db


class SessionRepository:
    @staticmethod
    def create(user_id: int, token: str, expires_at: datetime) -> Session:
        session = Session(
            user_id=user_id,
            token=token,
            expires_at=expires_at,
        )
        db.session.add(session)
        db.session.commit()
        return session

    @staticmethod
    def get_by_token(token: str) -> Session | None:
        return Session.query.filter_by(token=token).first()

    @staticmethod
    def get_active_by_token(token: str) -> Session | None:
        return Session.query.filter(
            Session.token == token,
            Session.expires_at > datetime.utcnow()
        ).first()

    @staticmethod
    def get_user_sessions(user_id: int) -> list[Session]:
        return Session.query.filter_by(user_id=user_id).all()

    @staticmethod
    def delete(session: Session) -> None:
        db.session.delete(session)
        db.session.commit()

    @staticmethod
    def delete_by_token(token: str) -> None:
        session = SessionRepository.get_by_token(token)
        if session:
            db.session.delete(session)
            db.session.commit()

    @staticmethod
    def delete_user_sessions(user_id: int) -> None:
        Session.query.filter_by(user_id=user_id).delete()
        db.session.commit()

    @staticmethod
    def delete_expired() -> int:
        result = Session.query.filter(
            Session.expires_at <= datetime.utcnow()
        ).delete()
        db.session.commit()
        return result