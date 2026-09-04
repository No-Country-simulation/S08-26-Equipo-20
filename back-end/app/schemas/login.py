from pydantic import BaseModel, Field, field_validator


class LoginRequest(BaseModel):
    email: str = Field(min_length=1)
    password: str = Field(min_length=8)

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        if "@" not in value:
            raise ValueError("el email debe contener un '@'")

        domain = value.split("@")[-1]
        if not domain or "." not in domain:
            raise ValueError("el email debe tener un dominio válido")

        return value