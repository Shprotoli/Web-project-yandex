from backend.other.extensions import db
from backend.db.models.question import Question


class QuestionRepository:
    @staticmethod
    def get_by_blitz(blitz_id: int) -> list[Question]:
        return Question.query.filter_by(blitz_id=blitz_id)\
            .order_by(Question.order_num.asc()).all()

    @staticmethod
    def get_by_id(question_id: int) -> Question | None:
        return db.session.get(Question, question_id)

    @staticmethod
    def create(question: Question) -> Question:
        db.session.add(question)
        db.session.commit()
        return question

    @staticmethod
    def update() -> None:
        db.session.commit()

    @staticmethod
    def delete(question: Question) -> None:
        db.session.delete(question)
        db.session.commit()