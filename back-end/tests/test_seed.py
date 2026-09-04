from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.config import settings
from app.core.security import verify_password
from app.database import Base
from app.models.role import Role
from app.models.user import User
from app.seed import seed


def build_session_factory():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    return sessionmaker(bind=engine)


def test_seed_creates_roles_and_admin():
    SessionFactory = build_session_factory()
    seed(SessionFactory)

    with SessionFactory() as db:
        admin = db.query(User).filter(User.email == settings.ADMIN_EMAIL).one()
        assert admin.role.name == "ADMIN"
        assert verify_password(settings.ADMIN_PASSWORD, admin.password_hash)


def test_seed_is_idempotent():
    SessionFactory = build_session_factory()
    seed(SessionFactory)
    seed(SessionFactory)

    with SessionFactory() as db:
        assert db.query(User).filter(User.email == settings.ADMIN_EMAIL).count() == 1
        assert db.query(Role).count() == 3