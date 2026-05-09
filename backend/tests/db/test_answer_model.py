import pytest
from backend.web.app import create_app
from backend.other.config import TestingConfig
from backend.other.extensions import db
from backend.db.models.blitz import Blitz
from backend.db.models.question import Question
from backend.db.models.answer import Answer


@pytest.fixture
def app():
    app = create_app()
    app.config.from_object(TestingConfig)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def question_id(app):
    with app.app_context():
        blitz = Blitz(
            id_subject="test-blitz-answer",
            title="Test Blitz for Answers",
            description="desc",
            path_file_blitz="file.txt"
        )
        db.session.add(blitz)
        db.session.commit()

        question = Question(
            blitz_id=blitz.id,
            text="Что такое ORM в SQLAlchemy?",
            order_num=1
        )
        db.session.add(question)
        db.session.commit()

        return question.id


def test_create_answer(app, question_id):
    with app.app_context():
        answer = Answer(
            question_id=question_id,
            text="Object-Relational Mapping",
            is_correct=True
        )
        db.session.add(answer)
        db.session.commit()

        assert answer.id is not None
        assert answer.question_id == question_id
        assert answer.text == "Object-Relational Mapping"
        assert answer.is_correct is True


def test_answer_repr(app, question_id):
    with app.app_context():
        answer = Answer(
            question_id=question_id,
            text="Test Answer",
            is_correct=False
        )
        db.session.add(answer)
        db.session.commit()

        expected_repr = f"<Answer {answer.id} for Q{question_id} (correct: False)>"
        assert repr(answer) == expected_repr


def test_multiple_answers_per_question(app, question_id):
    with app.app_context():
        answers = [
            Answer(question_id=question_id, text="Ответ 1", is_correct=True),
            Answer(question_id=question_id, text="Ответ 2", is_correct=False),
            Answer(question_id=question_id, text="Ответ 3", is_correct=False),
        ]
        db.session.add_all(answers)
        db.session.commit()

        loaded_question = db.session.get(Question, question_id)
        assert len(loaded_question.answers) == 3

        correct_count = sum(1 for a in loaded_question.answers if a.is_correct)
        assert correct_count == 1