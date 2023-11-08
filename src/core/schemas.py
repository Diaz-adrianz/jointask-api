from core.user.schema import User, UserDisplay, UserBoards
from core.board.schema import BoardDetail, Board
from core.board.member.schema import BoardMember, BoardMemberDetail
from core.task.schema import Task


# rebuild all schemas with relation
UserBoards.model_rebuild()
UserDisplay.model_rebuild()

BoardDetail.model_rebuild()
BoardMemberDetail.model_rebuild()

Task.model_rebuild()
