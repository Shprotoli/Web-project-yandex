from flask import Blueprint

from backend.api.schemas.serializers import session_to_dict, user_to_dict
from backend.api.services.auth_service import AuthService
from backend.api.utils.http import error_response, success_response
from backend.api.utils.request import (
    RequestValidationError,
    UnauthorizedError,
    get_bearer_token,
    get_json_body,
)
from backend.db.repositories.session_repository import SessionRepository

bp = Blueprint("auth_api", __name__)
auth_service = AuthService()


@bp.post("/auth/register")
def register():
    try:
        data = get_json_body(["username", "email", "password", "confirm_password"])
    except RequestValidationError as exc:
        return error_response(str(exc), status=400)

    user, errors = auth_service.register(data)
    if errors:
        return error_response("Ошибка валидации", status=422, errors=errors)

    return success_response(user_to_dict(user), status=201)


@bp.post("/auth/login")
def login():
    try:
        data = get_json_body(["username", "password"])
    except RequestValidationError as exc:
        return error_response(str(exc), status=400)

    user, session = auth_service.login(data["username"], data["password"])
    if user is None or session is None:
        return error_response("Неверный username или password", status=401)

    return success_response({
        "user": user_to_dict(user),
        "session": session_to_dict(session),
    }, status=201)


@bp.post("/auth/logout")
def logout():
    try:
        token = get_bearer_token()
    except UnauthorizedError as exc:
        return error_response(str(exc), status=401)

    active_session = SessionRepository.get_active_by_token(token)
    if active_session is None:
        return error_response("Активная сессия не найдена", status=404)

    SessionRepository.delete(active_session)
    return success_response({"message": "Выход выполнен"})


@bp.post("/auth/logout-all")
def logout_all():
    try:
        token = get_bearer_token()
    except UnauthorizedError as exc:
        return error_response(str(exc), status=401)

    user, _ = auth_service.get_current_user_by_token(token)
    if user is None:
        return error_response("Активная сессия не найдена", status=404)

    SessionRepository.delete_user_sessions(user.id)
    return success_response({"message": "Все сессии пользователя удалены"})


@bp.get("/users/me")
def me():
    try:
        token = get_bearer_token()
    except UnauthorizedError as exc:
        return error_response(str(exc), status=401)

    user, session = auth_service.get_current_user_by_token(token)
    if user is None or session is None:
        return error_response("Сессия недействительна или истекла", status=401)

    return success_response({
        "user": user_to_dict(user),
        "session": session_to_dict(session),
    })
