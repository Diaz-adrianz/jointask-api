from fastapi import APIRouter, Depends, middleware
from sqlalchemy.orm import Session
from core.auth.oauth2 import get_cred
from core.user import schema

from core.user.repo import UserRepo
from core.user import schema
from db.database import get_db

router = APIRouter(tags=["users"], prefix="/user")


@router.post("/create", response_model=schema.UserDisplay)
def create_user(req: schema.User, db: Session = Depends(get_db)):
    return UserRepo.create(db, req)


@router.get("/my", response_model=schema.UserDisplay)
def user_profile(
    db: Session = Depends(get_db), current_user: schema.User = Depends(get_cred())
):
    return UserRepo.get_user_by_id(db, current_user.id)


@router.patch("/my", response_model=schema.UserDisplay)
def create_user(
    req: schema.User,
    db: Session = Depends(get_db),
    current_user: schema.User = Depends(get_cred()),
):
    return UserRepo.update(db, current_user.id, req)


@router.get("/myboards")
def user_boards(
    db: Session = Depends(get_db), current_user: schema.User = Depends(get_cred())
):
    return UserRepo.get_user_boards(db, current_user.id)
