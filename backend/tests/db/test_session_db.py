from datetime import datetime, timedelta, UTC

import pytest
from sqlalchemy.exc import IntegrityError

from backend.web.app import create_app
from backend.other.config import TestingConfig
from backend.db.models.user import User
from backend.db.models.session import Session
from backend.other.extensions import db


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
def user_id(app):
    with app.app_context():
        user = User(username="test_user", email="test_user@example.com", password="hashed_password")
        db.session.add(user)
        db.session.commit()
        return user.id


def test_create_session(app, user_id):
    with app.app_context():
        session = Session(
            user_id=user_id,
            token="token_123",
            expires_at=datetime.now(UTC) + timedelta(days=1),
        )
        db.session.add(session)
        db.session.commit()

        saved_session = Session.query.filter_by(token="token_123").first()

        assert saved_session is not None
        assert saved_session.id is not None
        assert saved_session.user_id == user_id
        assert saved_session.token == "token_123"
        assert saved_session.created_at is not None


def test_session_requires_user_id(app):
    with app.app_context():
        session = Session(
            token="token_without_user",
            expires_at=datetime.now(UTC) + timedelta(days=1),
        )
        db.session.add(session)

        with pytest.raises(IntegrityError):
            db.session.commit()

        db.session.rollback()


def test_session_requires_token(app, user_id):
    with app.app_context():
        session = Session(
            user_id=user_id,
            expires_at=datetime.now(UTC) + timedelta(days=1),
        )
        db.session.add(session)

        with pytest.raises(IntegrityError):
            db.session.commit()

        db.session.rollback()


def test_session_token_must_be_unique(app, user_id):
    with app.app_context():
        session1 = Session(
            user_id=user_id,
            token="same_token",
            expires_at=datetime.now(UTC) + timedelta(days=1),
        )
        session2 = Session(
            user_id=user_id,
            token="same_token",
            expires_at=datetime.now(UTC) + timedelta(days=2),
        )

        db.session.add(session1)
        db.session.commit()

        db.session.add(session2)
        with pytest.raises(IntegrityError):
            db.session.commit()

        db.session.rollback()


def test_session_requires_expires_at(app, user_id):
    with app.app_context():
        session = Session(
            user_id=user_id,
            token="token_without_expires",
        )
        db.session.add(session)

        with pytest.raises(IntegrityError):
            db.session.commit()

        db.session.rollback()


def test_session_user_relationship(app, user_id):
    with app.app_context():
        session = Session(
            user_id=user_id,
            token="rel_token",
            expires_at=datetime.now(UTC) + timedelta(days=1),
        )
        db.session.add(session)
        db.session.commit()

        saved_session = Session.query.filter_by(token="rel_token").first()

        assert saved_session.user is not None
        assert saved_session.user.id == user_id
        assert saved_session.user.username == "test_user"


def test_user_sessions_backref(app, user_id):
    with app.app_context():
        session1 = Session(
            user_id=user_id,
            token="token_1",
            expires_at=datetime.now(UTC) + timedelta(days=1),
        )
        session2 = Session(
            user_id=user_id,
            token="token_2",
            expires_at=datetime.now(UTC) + timedelta(days=2),
        )

        db.session.add_all([session1, session2])
        db.session.commit()

        saved_user = db.session.get(User, user_id)

        assert saved_user.sessions is not None
        assert len(saved_user.sessions) == 2
        assert {session.token for session in saved_user.sessions} == {"token_1", "token_2"}