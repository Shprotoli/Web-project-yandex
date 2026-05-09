import pytest

from backend.web.app import create_app
from backend.other.config import TestingConfig
from backend.other.extensions import db
from backend.db.models.blitz import Blitz


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
        blitz = Blitz(
            title="Блитц тест",
            description="First blitz",
            path_file_blitz="blitz/",
            id_subject="blitz-test"
        )
        db.session.add(blitz)
        db.session.commit()

        found = Blitz.query.filter_by(title="Блитц тест").first()

        assert found is not None
        assert found.title == "Блитц тест"
        assert found.id_subject == "blitz-test"
