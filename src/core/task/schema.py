from datetime import datetime
from pydantic import BaseModel
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from core.board.schema import Board


class Task(BaseModel):
    id: Optional[str] = ""
    title: Optional[str] = ""
    priority: Optional[str] = ""
    is_done: Optional[bool] = False
    board_id: Optional[str] = ""
    board: "Board" = None
    updated_at: Optional[datetime] = ""
    created_at: Optional[datetime] = ""
