import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.core.security import hash_password
from app.database import Base, get_db
from app.main import app
from app.models.user import User


@pytest.fixture()
def client():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    TestingSessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    db = TestingSessionLocal()
    db.add(
        User(
            name="Admin",
            email="admin@serviceflow.com",
            password_hash=hash_password("Admin-123"),
            role_id=1,
        )
    )
    db.commit()
    db.close()

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()


def test_login_success(client):
    response = client.post(
        "/api/auth/login",
        json={"email": "admin@serviceflow.com", "password": "Admin-123"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["token_type"] == "bearer"
    assert body["access_token"]
    assert body["user"]["email"] == "admin@serviceflow.com"
    assert body["user"]["name"] == "Admin"


def test_login_wrong_password(client):
    response = client.post(
        "/api/auth/login",
        json={"email": "admin@serviceflow.com", "password": "Wrong-123"},
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Credenciales inválidas"


def test_login_email_not_found(client):
    response = client.post(
        "/api/auth/login",
        json={"email": "nobody@serviceflow.com", "password": "Admin-123"},
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Credenciales inválidas"


def test_login_case_insensitive_email(client):
    response = client.post(
        "/api/auth/login",
        json={"email": "ADMIN@serviceflow.com", "password": "Admin-123"},
    )

    assert response.status_code == 200


def test_login_invalid_payload(client):
    response = client.post(
        "/api/auth/login",
        json={"email": "admin@serviceflow.com", "password": "123"},
    )

    assert response.status_code == 422


def test_me_with_token(client):
    login = client.post(
        "/api/auth/login",
        json={"email": "admin@serviceflow.com", "password": "Admin-123"},
    )
    token = login.json()["access_token"]

    response = client.get(
        "/api/auth/me", headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["email"] == "admin@serviceflow.com"


def test_me_without_token(client):
    response = client.get("/api/auth/me")

    assert response.status_code == 401


def test_me_invalid_token(client):
    response = client.get(
        "/api/auth/me", headers={"Authorization": "Bearer token-invalido"}
    )

    assert response.status_code == 401