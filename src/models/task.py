import enum
import uuid
from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, String, func
from sqlalchemy.orm import relationship
from db.database import Base


class Priority(enum.Enum):
    important = "important"
    high = "high"
    normal = "normal"
    low = "low"


class Task(Base):
    __tablename__ = "tasks"

    id = Column(String(36), primary_key=True, default=uuid.uuid4)
    title = Column(String(255), nullable=False)
    priority = Column(Enum(Priority))
    is_done = Column(Boolean)

    board_id = Column(String, ForeignKey("boards.id"))
    board = relationship("Board", back_populates="tasks")

    created_at = Column(DateTime, default=func.now(), onupdate=func.now())
    updated_at = Column(DateTime, default=func.now())
