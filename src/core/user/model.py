import uuid

from sqlalchemy import Column, DateTime, String, func, text
from sqlalchemy.orm import relationship

from db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        String(36),
        primary_key=True,
        default=str(uuid.uuid4()),
        server_default=text("uuid_generate_v4()"),
    )
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    profile_picture = Column(String(255), nullable=True)

    owned_boards = relationship("Board", back_populates="owner")

    boards = relationship("BoardMember", back_populates="user")

    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    created_at = Column(DateTime, default=func.now())
