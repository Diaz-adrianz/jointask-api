from typing import List, TYPE_CHECKING, Optional
from pydantic import BaseModel

if TYPE_CHECKING:
    from core.user.schema import UserDisplay
    from core.task.schema import Task


class Board(BaseModel):
    id: Optional[str] = ""
    title: Optional[str] = ""
    description: Optional[str] = ""
    owner_id: Optional[str] = ""
    owner: "UserDisplay" = None
    members: List["UserDisplay"] = []
    tasks: List["Task"] = []
    created_at: Optional[str] = ""
    updated_at: Optional[str] = ""
