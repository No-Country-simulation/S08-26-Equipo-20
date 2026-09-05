import pytest
from pydantic import ValidationError

from app.models.user import User
from app.schemas import LoginRequest, Token, UserOut


def test_login_request_valid():
    data = LoginRequest(email="admin@serviceflow.com", password="secreto123")

    assert data.email == "admin@serviceflow.com"
    assert data.password == "secreto123"


def test_login_request_rejects_empty_fields():
    with pytest.raises(ValidationError):
        LoginRequest(email="", password="secreto123")

    with pytest.raises(ValidationError):
        LoginRequest(email="admin@serviceflow.com", password="")


def test_login_request_rejects_short_password():
    with pytest.raises(ValidationError):
        LoginRequest(email="admin@serviceflow.com", password="1234567")


def test_login_request_accepts_eight_character_password():
    data = LoginRequest(email="admin@serviceflow.com", password="12345678")

    assert data.password == "12345678"


def test_login_request_rejects_email_without_at():
    with pytest.raises(ValidationError, match="@"):
        LoginRequest(email="admin.serviceflow.com", password="secret123")


def test_login_request_rejects_email_without_domain():
    with pytest.raises(ValidationError, match="dominio"):
        LoginRequest(email="admin@", password="secret123")

    with pytest.raises(ValidationError, match="dominio"):
        LoginRequest(email="admin@serviceflow", password="secret123")


def test_token_default_token_type():
    token = Token(access_token="abc.def.ghi")

    assert token.token_type == "bearer"


def test_user_out_from_model():
    user = User(
        id=1,
        name="Admin",
        email="admin@serviceflow.com",
        password_hash="hash",
        role_id=1,
        team_id=None,
    )

    data = UserOut.model_validate(user)

    assert data.id == 1
    assert data.name == "Admin"
    assert data.email == "admin@serviceflow.com"
    assert data.role_id == 1
    assert data.team_id is None