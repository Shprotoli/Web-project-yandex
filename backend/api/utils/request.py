from flask import request

from backend.api.utils.http import error_response


class RequestValidationError(ValueError):
    pass


class UnauthorizedError(PermissionError):
    pass


def get_json_body(required_fields: list[str] | None = None) -> dict:
    data = request.get_json(silent=True)
    if data is None:
        raise RequestValidationError("Тело запроса должно быть валидным JSON")

    required_fields = required_fields or []
    missing_fields = [field for field in required_fields if data.get(field) in (None, "")]
    if missing_fields:
        raise RequestValidationError(
            f"Обязательные поля отсутствуют: {', '.join(missing_fields)}"
        )
    return data


def get_bearer_token() -> str:
    auth_header = request.headers.get("Authorization", "")
    prefix = "Bearer "
    if not auth_header.startswith(prefix):
        raise UnauthorizedError("Требуется Bearer token в заголовке Authorization")

    token = auth_header[len(prefix):].strip()
    if not token:
        raise UnauthorizedError("Bearer token пустой")
    return token
