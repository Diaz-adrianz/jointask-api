from fastapi import APIRouter, Depends
from core import schemas
from sqlalchemy.orm import Session
from core.auth.oauth2 import get_cred

from core.task.repo import TaskRepo
from db.database import get_db

router = APIRouter(tags=["Task"], prefix="/task")


@router.post("/", response_model=schemas.Task)
def create_task(
    req: schemas.Task,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_cred()),
):
    return TaskRepo.create(db, req, current_user.id)


@router.patch("/{task_id}")
def update_task_status(
    task_id: str,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_cred()),
):
    return TaskRepo.update_status(db, task_id, current_user.id)


@router.delete("/{task_id}")
def delete_task(
    task_id: str,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_cred()),
):
    return TaskRepo.delete(db, task_id, current_user.id)
