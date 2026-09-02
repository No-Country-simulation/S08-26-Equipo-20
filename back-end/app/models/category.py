from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(255), nullable=True)
    requires_approval = Column(Boolean, nullable=False, server_default="false")
