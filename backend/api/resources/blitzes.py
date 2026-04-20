from flask import Blueprint

from backend.api.schemas.serializers import blitz_to_dict
from backend.api.utils.http import error_response, success_response
from backend.api.utils.request import RequestValidationError, get_json_body
from backend.db.models.blitz import Blitz
from backend.db.repositories.blitz_repository import BlitzRepository

bp = Blueprint("blitzes_api", __name__)


@bp.get("/blitzes")
def get_blitzes():
    return success_response([blitz_to_dict(blitz) for blitz in BlitzRepository.get_all()])


@bp.post("/blitzes")
def create_blitz():
    try:
        data = get_json_body(["title", "description", "path_file_blitz"])
    except RequestValidationError as exc:
        return error_response(str(exc), status=400)

    if BlitzRepository.get_by_title(data["title"]):
        return error_response("Blitz с таким title уже существует", status=409)

    blitz = Blitz(
        title=data["title"],
        description=data["description"],
        path_file_blitz=data["path_file_blitz"],
    )
    BlitzRepository.create(blitz)
    return success_response(blitz_to_dict(blitz), status=201)


@bp.get("/blitzes/<int:blitz_id>")
def get_blitz(blitz_id: int):
    blitz = BlitzRepository.get_by_id(blitz_id)
    if blitz is None:
        return error_response("Blitz не найден", status=404)
    return success_response(blitz_to_dict(blitz))


@bp.put("/blitzes/<int:blitz_id>")
def update_blitz(blitz_id: int):
    blitz = BlitzRepository.get_by_id(blitz_id)
    if blitz is None:
        return error_response("Blitz не найден", status=404)

    try:
        data = get_json_body(["title", "description", "path_file_blitz"])
    except RequestValidationError as exc:
        return error_response(str(exc), status=400)

    existing = BlitzRepository.get_by_title(data["title"])
    if existing and existing.id != blitz_id:
        return error_response("Blitz с таким title уже существует", status=409)

    blitz.title = data["title"]
    blitz.description = data["description"]
    blitz.path_file_blitz = data["path_file_blitz"]
    BlitzRepository.update()

    return success_response(blitz_to_dict(blitz))


@bp.patch("/blitzes/<int:blitz_id>")
def patch_blitz(blitz_id: int):
    blitz = BlitzRepository.get_by_id(blitz_id)
    if blitz is None:
        return error_response("Blitz не найден", status=404)

    try:
        data = get_json_body()
    except RequestValidationError as exc:
        return error_response(str(exc), status=400)

    if "title" in data:
        existing = BlitzRepository.get_by_title(data["title"])
        if existing and existing.id != blitz_id:
            return error_response("Blitz с таким title уже существует", status=409)
        blitz.title = data["title"]
    if "description" in data:
        blitz.description = data["description"]
    if "path_file_blitz" in data:
        blitz.path_file_blitz = data["path_file_blitz"]

    BlitzRepository.update()
    return success_response(blitz_to_dict(blitz))


@bp.delete("/blitzes/<int:blitz_id>")
def delete_blitz(blitz_id: int):
    blitz = BlitzRepository.get_by_id(blitz_id)
    if blitz is None:
        return error_response("Blitz не найден", status=404)

    BlitzRepository.delete(blitz)
    return "", 204
