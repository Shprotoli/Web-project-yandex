from flask import Flask, send_from_directory
from flask_cors import CORS

from backend.other.config import DevelopmentConfig
from backend.other.extensions import db, migrate
from backend.api import register_api


def create_app(config_object=DevelopmentConfig):
    app = Flask(__name__,
                static_folder='static/build/',
                static_url_path='',
                template_folder='static/build/')

    app.config.from_object(config_object)

    CORS(app,
         origins="*",
         methods="*",
         allow_headers="*",
         supports_credentials=True)

    db.init_app(app)
    migrate.init_app(app, db)

    register_api(app)

    @app.route('/')
    def serve_index():
        return send_from_directory(app.template_folder, 'index.html')

    @app.route('/<path:path>')
    def serve_static(path):
        try:
            return send_from_directory(app.static_folder, path)
        except FileNotFoundError:
            return send_from_directory(app.template_folder, 'index.html')

    return app


if __name__ == "__main__":
    app = create_app()

    with app.app_context():
        import backend.db.models.question
        import backend.db.models.answer
        import backend.db.models.blitz
        import backend.db.models.user
        import backend.db.models.session
        db.create_all()

    app.run(host='0.0.0.0', port=8080, debug=True)
