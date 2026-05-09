from backend.other.extensions import db
from backend.db.models.answer import Answer


class AnswerRepository:
    @staticmethod
    def get_by_question(question_id: int) -> list[Answer]:
        return Answer.query.filter_by(question_id=question_id).all()

    @staticmethod
    def get_by_id(answer_id: int) -> Answer | None:
        return db.session.get(Answer, answer_id)

    @staticmethod
    def get_correct_answers(question_id: int) -> list[Answer]:
        return Answer.query.filter_by(
            question_id=question_id,
            is_correct=True
        ).all()

    @staticmethod
    def is_correct(answer_id: int) -> bool:
        answer = db.session.get(Answer, answer_id)
        return answer.is_correct if answer else False

    @staticmethod
    def check_user_answer(question_id: int, selected_answer_id: int) -> bool:
        correct_answers = AnswerRepository.get_correct_answers(question_id)
        return any(answer.id == selected_answer_id for answer in correct_answers)

    @staticmethod
    def create(answer: Answer) -> Answer:
        db.session.add(answer)
        db.session.commit()
        return answer

    @staticmethod
    def update() -> None:
        db.session.commit()

    @staticmethod
    def delete(answer: Answer) -> None:
        db.session.delete(answer)
        db.session.commit()