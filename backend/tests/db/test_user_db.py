import pytest

from backend.other.config import TestingConfig
from backend.web.app import create_app
from backend.other.extensions import db
from backend.db.models.user import User


@pytest.fixture
def app():
    app = create_app()
    app.config.from_object(TestingConfig)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


def test_create_user(app):
    with app.app_context():
        user = User(username="alex", email="alex@example.com", password="123")
        db.session.add(user)
        db.session.commit()

        found = User.query.filter_by(username="alex").first()

        assert found is not None
        assert found.username == "alex"
