from core.user.schema import UserBoards, UserDisplay
from core.task.schema import Task
from core.board.schema import BoardDetail, Board

UserBoards.model_rebuild()
UserDisplay.model_rebuild()
Task.model_rebuild()
Board.model_rebuild()
BoardDetail.model_rebuild()
