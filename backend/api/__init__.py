from backend.api.resources.auth import bp as auth_bp
from backend.api.resources.blitzes import bp as blitzes_bp
from backend.api.resources.sessions import bp as sessions_bp
from backend.api.resources.users import bp as users_bp


def register_api(app):
    @app.get("/health")
    def healthcheck():
        return {"success": True, "data": {"status": "ok"}}, 200

    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(sessions_bp)
    app.register_blueprint(blitzes_bp)