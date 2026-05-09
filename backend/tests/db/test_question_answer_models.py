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
def blitz_id(app):
    with app.app_context():
        b = Blitz(
            id_subject="test-blitz",
            title="Test Blitz",
            description="Test description",
            path_file_blitz="blitz/test.txt"
        )
        db.session.add(b)
        db.session.commit()
        return b.id


def test_create_question(app, blitz_id):
    with app.app_context():
        question = Question(
            blitz_id=blitz_id,
            text="Что такое Python?",
            order_num=1
        )
        db.session.add(question)
        db.session.commit()

        assert question.id is not None
        assert question.blitz_id == blitz_id
        assert question.text == "Что такое Python?"


def test_question_relationship_with_blitz(app, blitz_id):
    with app.app_context():
        q = Question(blitz_id=blitz_id, text="Q1", order_num=1)
        db.session.add(q)
        db.session.commit()

        blitz = db.session.get(Blitz, blitz_id)
        assert len(blitz.questions) == 1
        assert blitz.questions[0].text == "Q1"


def test_create_answer(app, blitz_id):
    with app.app_context():
        question = Question(
            blitz_id=blitz_id,
            text="Какой язык программирования используется для веб-разработки?",
            order_num=1
        )
        db.session.add(question)
        db.session.commit()

        answer1 = Answer(question_id=question.id, text="Python", is_correct=True)
        answer2 = Answer(question_id=question.id, text="Java", is_correct=False)

        db.session.add_all([answer1, answer2])
        db.session.commit()

        assert answer1.is_correct is True
        assert answer2.is_correct is False
        assert len(question.answers) == 2


def test_answer_relationship_with_question(app, blitz_id):
    with app.app_context():
        q = Question(blitz_id=blitz_id, text="Q", order_num=1)
        db.session.add(q)
        db.session.commit()

        a = Answer(question_id=q.id, text="Правильный ответ", is_correct=True)
        db.session.add(a)
        db.session.commit()

        loaded_question = db.session.get(Question, q.id)
        assert len(loaded_question.answers) == 1
        assert loaded_question.answers[0].text == "Правильный ответ"
