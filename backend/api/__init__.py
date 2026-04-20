from flask import Blueprint

from backend.api.resources.auth import bp as auth_bp
from backend.api.resources.blitzes import bp as blitzes_bp
from backend.api.resources.sessions import bp as sessions_bp
from backend.api.resources.users import bp as users_bp


def register_api(app):
    api_bp = Blueprint("api_v1", __name__, url_prefix="/api/v1")

    @api_bp.get("/health")
    def healthcheck():
        return {"success": True, "data": {"status": "ok"}}, 200

    api_bp.register_blueprint(auth_bp)
    api_bp.register_blueprint(users_bp)
    api_bp.register_blueprint(sessions_bp)
    api_bp.register_blueprint(blitzes_bp)

    app.register_blueprint(api_bp)
