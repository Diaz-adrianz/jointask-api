from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session

from core import schemas
from core.board.repo import BoardRepo
from . import model


class TaskRepo:
    def get_by_id(db: Session, id: str):
        task = db.query(model.Task).filter(model.Task.id == (id)).first()

        if not task:
            raise HTTPException(status_code=404, detail=f"Task with Id {id} not found")

        return task

    def update_status(db: Session, task_id: str, user_id: str):
        task = TaskRepo.get_by_id(db, task_id)

        if not BoardRepo.is_user_have_acces(db, task.board_id, user_id):
            return

        task.is_done = not task.is_done

        try:
            db.commit()
            db.refresh(task)

            return task

        except IntegrityError as e:
            db.rollback()

            print(e)
            raise HTTPException(status_code=500, detail="Internal server error")

    def create(db: Session, req: schemas.Task, user_id: str):
        if not BoardRepo.is_user_have_acces(db, req.board_id, user_id):
            return

        new_task = model.Task(
            title=req.title, priority=req.priority, board_id=req.board_id
        )

        try:
            db.add(new_task)
            db.commit()
            db.refresh(new_task)

            return new_task

        except IntegrityError as e:
            db.rollback()

            print(e)
            raise HTTPException(status_code=500, detail="Internal server error")

    def delete(db: Session, task_id: str, user_id: str):
        task: schemas.Task = TaskRepo.get_by_id(db, task_id)

        if not BoardRepo.is_user_have_acces(db, task.board_id, user_id):
            return

        try:
            db.delete(task)
            db.commit()

            return {"detail": "Task deleted successfully"}

        except IntegrityError as e:
            db.rollback()

            print(e)
            raise HTTPException(status_code=500, detail="Internal server error")
