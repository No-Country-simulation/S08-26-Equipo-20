from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.database import Base


class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(Text, nullable=False)
    status = Column(String(20), nullable=False, server_default="NEW")
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    priority_id = Column(Integer, ForeignKey("priorities.id"), nullable=True)
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=True)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    assigned_to = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    resolved_at = Column(DateTime(timezone=True), nullable=True)
    closed_at = Column(DateTime(timezone=True), nullable=True)

    category = relationship("Category")
    priority = relationship("Priority")
    team = relationship("Team")
    creator = relationship("User", foreign_keys=[created_by])
    assignee = relationship("User", foreign_keys=[assigned_to])
