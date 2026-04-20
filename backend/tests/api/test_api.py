from backend.other.config import TestingConfig
from backend.other.extensions import db
from backend.web.app import create_app


def build_client():
    app = create_app(TestingConfig)
    with app.app_context():
        db.create_all()
    return app.test_client(), app


def test_full_auth_and_blitz_flow():
    client, app = build_client()

    register_response = client.post(
        "/api/v1/auth/register",
        json={
            "username": "alex",
            "email": "alex@example.com",
            "password": "strongpass123",
            "confirm_password": "strongpass123",
        },
    )
    assert register_response.status_code == 201

    login_response = client.post(
        "/api/v1/auth/login",
        json={"username": "alex", "password": "strongpass123"},
    )
    assert login_response.status_code == 201
    token = login_response.get_json()["data"]["session"]["token"]

    me_response = client.get(
        "/api/v1/users/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert me_response.status_code == 200
    assert me_response.get_json()["data"]["user"]["username"] == "alex"

    blitz_response = client.post(
        "/api/v1/blitzes",
        json={
            "title": "First blitz",
            "description": "Demo blitz",
            "path_file_blitz": "blitz/demo.pdf",
        },
    )
    assert blitz_response.status_code == 201

    list_response = client.get("/api/v1/blitzes")
    assert list_response.status_code == 200
    assert len(list_response.get_json()["data"]) == 1

    logout_response = client.post(
        "/api/v1/auth/logout",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert logout_response.status_code == 200

    with app.app_context():
        db.session.remove()
        db.drop_all()
