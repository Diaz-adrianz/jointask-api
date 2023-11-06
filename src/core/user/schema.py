from datetime import datetime
from pydantic import BaseModel
from typing import List, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from core.board.schema import Board


class User(BaseModel):
    id: Optional[str] = ""
    name: Optional[str] = ""
    email: Optional[str] = ""
    password: Optional[str] = ""
    profile_picture: Optional[str] = ""


class UserBoards(BaseModel):
    owned_boards: List["Board"] = []
    boards: List["Board"] = []


class UserDisplay(BaseModel):
    id: Optional[str] = ""
    name: Optional[str] = ""
    email: Optional[str] = ""
    profile_picture: Optional[str] = ""
    created_at: Optional[datetime] = ""
    updated_at: Optional[datetime] = ""
