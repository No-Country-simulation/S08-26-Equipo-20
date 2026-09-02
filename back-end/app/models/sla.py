from sqlalchemy import Column, Integer, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from app.database import Base


class SLA(Base):
    __tablename__ = "slas"

    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(Integer, ForeignKey("requests.id"), nullable=False)
    response_deadline = Column(DateTime(timezone=True), nullable=False)
    resolution_deadline = Column(DateTime(timezone=True), nullable=False)
    responded_at = Column(DateTime(timezone=True), nullable=True)
    resolved_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    request = relationship("Request", uselist=False)
