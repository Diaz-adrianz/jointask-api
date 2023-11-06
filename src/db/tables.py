import core.user.model
import core.board.model
import core.task.model

from .database import Base, engine

Base.metadata.create_all(engine)


def drop_all():
    Base.metadata.drop_all(engine)
