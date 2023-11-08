from typing import List
from fastapi import APIRouter, Depends, middleware
from sqlalchemy.orm import Session
from core.auth.oauth2 import get_cred

from core.user.repo import UserRepo
from core import schemas
from db.database import get_db

router = APIRouter(tags=["users"], prefix="/user")


@router.post("/", response_model=List[schemas.UserDisplay])
def browse_users(db: Session = Depends(get_db)):
    return UserRepo.browse(db)


@router.post("/create", response_model=schemas.UserDisplay)
def create_user(req: schemas.User, db: Session = Depends(get_db)):
    return UserRepo.create(db, req)


@router.get("/my", response_model=schemas.UserDisplay)
def user_profile(
    db: Session = Depends(get_db), current_user: schemas.User = Depends(get_cred())
):
    return UserRepo.get_user_by_id(db, current_user.id)


@router.patch("/my", response_model=schemas.UserDisplay)
def update_user(
    req: schemas.User,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_cred()),
):
    return UserRepo.update(db, current_user.id, req)
