from flask import Flask

from backend.other.config import DevelopmentConfig
from backend.other.extensions import db, migrate

# Models
from backend.db.models.user import User


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    migrate.init_app(app, db)

    return app


if __name__ == "__main__":
    app = create_app()

    with app.app_context():
        db.create_all()

    app.run(port=8080, debug=True)