from typing import Tuple

from flask import jsonify, Response


def success_response(data=None, status: int = 200) -> Tuple[Response, int]:
    payload = {"success": True}
    if data is not None:
        payload["data"] = data
    return jsonify(payload), status


def error_response(message: str, *, status: int = 400, errors=None) -> Tuple[Response, int]:
    payload = {
        "success": False,
        "message": message,
    }
    if errors is not None:
        payload["errors"] = errors
    return jsonify(payload), status
