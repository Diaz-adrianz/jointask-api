import uuid
from sqlalchemy import Column, DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import relationship
from db.database import Base


class BoardMember(Base):
    __tablename__ = "board_members"

    id = Column(String(36), primary_key=True, default=uuid.uuid4)

    user_id = Column(String, ForeignKey("users.id"))
    user = relationship("User", back_populates="boards")

    board_id = Column(String, ForeignKey("boards.id"))
    board = relationship("Board", back_populates="members")


class Board(Base):
    __tablename__ = "boards"

    id = Column(String(36), primary_key=True, default=uuid.uuid4)
    title = Column(String(255), nullable=False)
    description = Column(Text)

    owner_id = Column(String, ForeignKey("users.id"))
    owner = relationship("User", back_populates="owned_boards")

    members = relationship("BoardMember", back_populates="board")

    tasks = relationship("Task", back_populates="board")

    created_at = Column(DateTime, default=func.now(), onupdate=func.now())
    updated_at = Column(DateTime, default=func.now())
