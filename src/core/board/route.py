from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.auth.oauth2 import get_cred
from core.board.repo import BoardRepo

from db.database import get_db

from . import schema
from core.user.schema import User as UserSchema

router = APIRouter(tags=["Boards"], prefix="/board")


@router.get("/", response_model=List[schema.Board])
def get_all_board(db: Session = Depends(get_db)):
    return BoardRepo.get_all(db)


@router.get("/{id}", response_model=schema.BoardDetail)
def get_board_detail(id: str, db: Session = Depends(get_db)):
    return BoardRepo.get_by_id(db, id)


@router.post("/", response_model=schema.BoardDetail)
def create_board(
    req: schema.Board,
    db: Session = Depends(get_db),
    current_user: UserSchema = Depends(get_cred()),
):
    return BoardRepo.create(db, req, current_user.id)
