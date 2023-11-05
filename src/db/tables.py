import models.user
import models.board
import models.task

from .database import Base, engine

Base.metadata.create_all(engine)


def drop_all():
    Base.metadata.drop_all(engine)
