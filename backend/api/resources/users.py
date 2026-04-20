from flask import Blueprint

from backend.api.schemas.serializers import session_to_dict, user_to_dict
from backend.api.utils.http import error_response, success_response
from backend.db.repositories.session_repository import SessionRepository
from backend.db.repositories.user_repository import UserRepository

bp = Blueprint("users_api", __name__)


@bp.get("/users")
def get_users():
    users = [user_to_dict(user) for user in UserRepository.get_all()]
    return success_response(users)


@bp.get("/users/<int:user_id>")
def get_user(user_id: int):
    user = UserRepository.get_by_id(user_id)
    if user is None:
        return error_response("Пользователь не найден", status=404)
    return success_response(user_to_dict(user))


@bp.get("/users/<int:user_id>/sessions")
def get_user_sessions(user_id: int):
    user = UserRepository.get_by_id(user_id)
    if user is None:
        return error_response("Пользователь не найден", status=404)

    sessions = [session_to_dict(session) for session in SessionRepository.get_user_sessions(user_id)]
    return success_response(sessions)
