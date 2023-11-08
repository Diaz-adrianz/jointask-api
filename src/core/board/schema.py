from datetime import datetime
from typing import List, TYPE_CHECKING, Optional
from pydantic import BaseModel, RootModel


if TYPE_CHECKING:
    from core.board.member.schema import BoardMemberDetail
    from core.user.schema import UserDisplay
    from core.task.schema import Task


class Board(BaseModel):
    id: Optional[str] = ""
    title: Optional[str] = ""
    description: Optional[str] = ""


class BoardDetail(Board):
    owner_id: Optional[str] = ""
    owner: "UserDisplay" = None
    members: List["BoardMemberDetail"] = []
    tasks: List["Task"] = []
    created_at: Optional[datetime] = ""
    updated_at: Optional[datetime] = ""
