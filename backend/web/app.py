from flask import Flask

from backend.other.config import DevelopmentConfig
from backend.other.extensions import db, migrate
from backend.api import register_api

# Models
from backend.db.models.user import User
from backend.db.models.blitz import Blitz
from backend.db.models.session import Session

from flask import Blueprint
from backend.api.resources.auth import bp as auth_bp
from backend.api.resources.blitzes import bp as blitzes_bp
from backend.api.resources.sessions import bp as sessions_bp
from backend.api.resources.users import bp as users_bp


def create_app(config_object=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)
    migrate.init_app(app, db)
    register_api(app)

    return app


if __name__ == "__main__":
    app = create_app()

    with app.app_context():
        db.create_all()

    app.run(port=8080, debug=True)
