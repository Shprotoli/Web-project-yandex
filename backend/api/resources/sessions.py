from flask import Blueprint

from backend.api.schemas.serializers import session_to_dict
from backend.api.utils.http import error_response, success_response
from backend.db.models.session import Session
from backend.db.repositories.session_repository import SessionRepository
from backend.other.extensions import db

bp = Blueprint("sessions_api", __name__)


@bp.get("/sessions")
def get_sessions():
    sessions = Session.query.order_by(Session.id.asc()).all()
    return success_response([session_to_dict(session) for session in sessions])


@bp.get("/sessions/<int:session_id>")
def get_session(session_id: int):
    session = db.session.get(Session, session_id)
    if session is None:
        return error_response("Сессия не найдена", status=404)
    return success_response(session_to_dict(session))


@bp.delete("/sessions/<int:session_id>")
def delete_session(session_id: int):
    session = db.session.get(Session, session_id)
    if session is None:
        return error_response("Сессия не найдена", status=404)

    SessionRepository.delete(session)
    return "", 204


@bp.delete("/sessions/expired")
def delete_expired_sessions():
    deleted_count = SessionRepository.delete_expired()
    return success_response({"deleted": deleted_count})
