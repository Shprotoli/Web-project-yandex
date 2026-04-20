from flask import Flask

from backend.api import register_api
from backend.other.config import DevelopmentConfig
from backend.other.extensions import db, migrate

# Models
from backend.db.models.user import User
from backend.db.models.blitz import Blitz
from backend.db.models.session import Session


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
