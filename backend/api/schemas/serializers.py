from backend.db.models.blitz import Blitz
from backend.db.models.session import Session
from backend.db.models.user import User


def user_to_dict(user: User) -> dict:
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "created_at": user.created_at.isoformat() if user.created_at else None,
    }


def session_to_dict(session: Session) -> dict:
    return {
        "id": session.id,
        "user_id": session.user_id,
        "token": session.token,
        "created_at": session.created_at.isoformat() if session.created_at else None,
        "expires_at": session.expires_at.isoformat() if session.expires_at else None,
    }


def blitz_to_dict(blitz: Blitz) -> dict:
    return {
        "id": blitz.id,
        "title": blitz.title,
        "description": blitz.description,
        "path_file_blitz": blitz.path_file_blitz,
        "created_at": blitz.created_at.isoformat() if blitz.created_at else None,
    }
