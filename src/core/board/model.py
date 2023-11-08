import uuid
from sqlalchemy import Column, DateTime, ForeignKey, String, Text, func, text
from sqlalchemy.orm import relationship
from db.database import Base


class Board(Base):
    __tablename__ = "boards"

    id = Column(
        String(36),
        primary_key=True,
        default=str(uuid.uuid4()),
        # server_default=text("uuid_generate_v4()"),
    )
    title = Column(String(255), nullable=False)
    description = Column(Text)

    owner_id = Column(String, ForeignKey("users.id"))
    owner = relationship("User", back_populates="owned_boards")

    members = relationship("BoardMember", back_populates="board")

    tasks = relationship("Task", back_populates="board", cascade="all, delete-orphan")

    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    created_at = Column(DateTime, default=func.now())
