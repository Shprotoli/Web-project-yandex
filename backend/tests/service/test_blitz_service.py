import pytest
from backend.web.app import create_app
from backend.other.config import TestingConfig
from backend.other.extensions import db
from backend.web.service.blitz_service import BlitzService
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
def blitz_with_questions(app):
    with app.app_context():
        blitz = Blitz(
            id_subject="test-service-blitz",
            title="Service Test Blitz",
            description="Тест для BlitzService",
            path_file_blitz="test.txt"
        )
        db.session.add(blitz)
        db.session.commit()

        q1 = Question(blitz_id=blitz.id, text="Столица Франции?", order_num=1)
        db.session.add(q1)
        db.session.commit()

        a11 = Answer(question_id=q1.id, text="Париж", is_correct=True)
        a12 = Answer(question_id=q1.id, text="Лондон", is_correct=False)
        a13 = Answer(question_id=q1.id, text="Берлин", is_correct=False)
        db.session.add_all([a11, a12, a13])

        q2 = Question(blitz_id=blitz.id, text="2 + 2 = ?", order_num=2)
        db.session.add(q2)
        db.session.commit()

        a21 = Answer(question_id=q2.id, text="4", is_correct=True)
        a22 = Answer(question_id=q2.id, text="5", is_correct=False)
        db.session.add_all([a21, a22])

        db.session.commit()

        return blitz.id


def test_check_blitz_all_correct(app, blitz_with_questions):
    with app.app_context():
        user_answers = {1: 1, 2: 4}

        result = BlitzService.check_blitz_answers(blitz_with_questions, user_answers)

        assert result["total_questions"] == 2
        assert result["correct_answers"] == 2
        assert result["score_percent"] == 100.0


def test_check_blitz_all_wrong(app, blitz_with_questions):
    with app.app_context():
        user_answers = {1: 2, 2: 5}

        result = BlitzService.check_blitz_answers(blitz_with_questions, user_answers)

        assert result["total_questions"] == 2
        assert result["correct_answers"] == 0
        assert result["score_percent"] == 0.0


def test_check_blitz_partial_correct(app, blitz_with_questions):
    with app.app_context():
        user_answers = {1: 1, 2: 5}

        result = BlitzService.check_blitz_answers(blitz_with_questions, user_answers)

        assert result["total_questions"] == 2
        assert result["correct_answers"] == 1
        assert result["score_percent"] == 50.0


def test_check_blitz_missing_answers(app, blitz_with_questions):
    with app.app_context():
        user_answers = {1: 1}

        result = BlitzService.check_blitz_answers(blitz_with_questions, user_answers)

        assert result["total_questions"] == 2
        assert result["correct_answers"] == 1
        assert result["score_percent"] == 50.0


def test_check_blitz_not_found(app):
    with app.app_context():
        result = BlitzService.check_blitz_answers(9999, {})
        assert "error" in result


def test_check_blitz_empty_answers(app, blitz_with_questions):
    with app.app_context():
        result = BlitzService.check_blitz_answers(blitz_with_questions, {})

        assert result["total_questions"] == 2
        assert result["correct_answers"] == 0
        assert result["score_percent"] == 0.0