from datetime import datetime
from typing import List, TYPE_CHECKING, Optional
from pydantic import BaseModel

if TYPE_CHECKING:
    from core.board.schema import Board
    from core.user.schema import UserDisplay


class BoardMember(BaseModel):
    id: Optional[str] = ""
    user_id: Optional[str] = ""
    board_id: Optional[str] = ""


class BoardMemberDetail(BoardMember):
    user: "UserDisplay" = None
    # board: "Board" = None
    joined_at: Optional[datetime] = ""
