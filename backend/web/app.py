from flask import Flask
from flask_cors import CORS
from flask import request

from backend.other.config import DevelopmentConfig
from backend.other.extensions import db, migrate
from backend.api import register_api

# Models
from backend.db.models.user import User
from backend.db.models.blitz import Blitz
from backend.db.models.session import Session
from backend.db.models.question import Question
from backend.db.models.answer import Answer

from flask import Blueprint
from backend.api.resources.auth import bp as auth_bp
from backend.api.resources.blitzes import bp as blitzes_bp
from backend.api.resources.sessions import bp as sessions_bp
from backend.api.resources.users import bp as users_bp


def create_app(config_object=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)

    # Отключаем все ограничения
    CORS(app, origins="*", methods="*", allow_headers="*", supports_credentials=True)

    db.init_app(app)
    migrate.init_app(app, db)
    register_api(app)

    # Ловим ВСЕ OPTIONS запросы глобально
    @app.before_request
    def handle_options():
        if request.method == 'OPTIONS':
            resp = app.make_response('')
            resp.headers['Access-Control-Allow-Origin'] = request.headers.get('Origin', '*')
            resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
            resp.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
            resp.headers['Access-Control-Allow-Credentials'] = 'true'
            return resp

    return app


if __name__ == "__main__":
    app = create_app()

    with app.app_context():
        db.create_all()

    app.run(port=8080, debug=True)
