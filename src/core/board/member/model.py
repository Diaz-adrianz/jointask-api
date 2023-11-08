import uuid
from sqlalchemy import Column, DateTime, ForeignKey, String, func, text
from sqlalchemy.orm import relationship
from db.database import Base


class BoardMember(Base):
    __tablename__ = "board_members"

    id = Column(
        String(36),
        primary_key=True,
        default=str(uuid.uuid4()),
        # server_default=text("uuid_generate_v4()"),
    )
    user_id = Column(String, ForeignKey("users.id"))
    user = relationship("User", back_populates="boards")
    board_id = Column(String, ForeignKey("boards.id"))
    board = relationship("Board", back_populates="members")
    joined_at = Column(DateTime, default=func.now())
