from core.user.schema import UserBoards
from core.task.schema import Task
from core.board.schema import Board

UserBoards.model_rebuild()
Task.model_rebuild()
Board.model_rebuild()
