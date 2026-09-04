from datetime import timedelta

import jwt
import pytest

from app.core.security import (
    create_access_token,
    decode_token,
    hash_password,
    verify_password,
)


def test_hash_and_verify_password():
    hashed = hash_password("Mi-Contrasena-123")

    assert hashed != "Mi-Contrasena-123"
    assert verify_password("Mi-Contrasena-123", hashed)
    assert not verify_password("Contrasena-incorrecta", hashed)


def test_create_and_decode_token():
    token = create_access_token(subject="42")

    assert decode_token(token) == "42"


def test_decode_expired_token_raises():
    expired = create_access_token(
        subject="42", expires_delta=timedelta(minutes=-1)
    )

    with pytest.raises(jwt.ExpiredSignatureError):
        decode_token(expired)