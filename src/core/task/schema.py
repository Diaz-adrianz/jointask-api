from datetime import datetime
from pydantic import BaseModel
from typing import TYPE_CHECKING, Optional

from core.task.model import Priority


class Task(BaseModel):
    id: Optional[str] = ""
    title: Optional[str] = ""
    priority: Optional[Priority] = Priority.normal
    is_done: Optional[bool] = False
    board_id: Optional[str] = ""
    updated_at: Optional[datetime] = ""
    created_at: Optional[datetime] = ""
