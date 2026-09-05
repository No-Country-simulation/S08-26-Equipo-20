from typing import Callable

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.config import settings
from app.core.security import hash_password
from app.database import SessionLocal
from app.models.role import Role
from app.models.user import User


def seed(session_factory: Callable[[], Session] = SessionLocal) -> None:
    if len(settings.ADMIN_PASSWORD) < 8:
        raise ValueError("ADMIN_PASSWORD debe tener al menos 8 caracteres")

    with session_factory() as db:
        for role_name in ("ADMIN", "AGENT", "USER"):
            if not db.scalar(select(Role).where(Role.name == role_name)):
                db.add(Role(name=role_name))
                print(f"seed: rol '{role_name}' creado")
        db.flush()

        admin_role = db.scalar(select(Role).where(Role.name == "ADMIN"))
        admin = db.scalar(
            select(User).where(func.lower(User.email) == settings.ADMIN_EMAIL.lower())
        )

        if not admin:
            db.add(
                User(
                    name="Administrador",
                    email=settings.ADMIN_EMAIL,
                    password_hash=hash_password(settings.ADMIN_PASSWORD),
                    role_id=admin_role.id,
                )
            )
            print(f"seed: usuario admin '{settings.ADMIN_EMAIL}' creado")
        else:
            print(f"seed: usuario admin '{settings.ADMIN_EMAIL}' ya existía")

        db.commit()


if __name__ == "__main__":
    seed()