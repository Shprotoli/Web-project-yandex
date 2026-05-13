from flask import Blueprint

from backend.api.schemas.serializers import blitz_to_dict
from backend.api.utils.http import error_response, success_response
from backend.api.utils.request import RequestValidationError, get_json_body
from backend.db.models.blitz import Blitz
from backend.db.repositories.blitz_repository import BlitzRepository
from backend.db.repositories.question_repository import QuestionRepository

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

    id_subject = data.get("id_subject") or f"blitz-{data['title'].lower().replace(' ', '-')[:30]}"

    blitz = Blitz(
        id_subject=id_subject,
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

    questions = QuestionRepository().get_by_blitz(blitz_id)

    result = blitz_to_dict(blitz)
    result["questions"] = []

    for question in questions:
        question_dict = {
            "id": question.id,
            "text": question.text,
            "order_num": question.order_num,
            "answers": []
        }

        for answer in question.answers:
            question_dict["answers"].append({
                "id": answer.id,
                "text": answer.text,
                "is_correct": answer.is_correct,
            })

        result["questions"].append(question_dict)

    return success_response(result)


@bp.post("/blitzes/<int:blitz_id>/submit")
def submit_blitz_answers(blitz_id: int):
    try:
        data = get_json_body(["answers"])
    except RequestValidationError as exc:
        return error_response(str(exc), status=400)

    user_answers = data["answers"]

    if not isinstance(user_answers, dict):
        return error_response("answers должен быть объектом", status=400)

    from backend.web.service.blitz_service import BlitzService

    result = BlitzService.check_blitz_answers(blitz_id, user_answers)

    if "error" in result:
        return error_response(result["error"], status=404)

    return success_response(result, status=200)


@bp.get("/blitzes/subject/<string:id_subject>")
def get_blitz_by_id_subject(id_subject: str):
    print(id_subject)
    blitzes = BlitzRepository.get_by_id_subject(id_subject)

    if not blitzes:
        return error_response(f"Blitz [id_subject={id_subject}] не найдены", status=404)

    if isinstance(blitzes, list):
        data = [blitz_to_dict(b) for b in blitzes]
    else:
        data = blitz_to_dict(blitzes)

    return success_response(data)


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
