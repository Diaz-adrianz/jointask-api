from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.auth.oauth2 import get_cred
from core.board.repo import BoardRepo

from db.database import get_db
from core import schemas

router = APIRouter(tags=["Boards"], prefix="/board")


@router.get("/", response_model=List[schemas.Board])
def get_all_board(db: Session = Depends(get_db)):
    return BoardRepo.get_all(db)


@router.get("/my")
def get_current_user_boards(
    db: Session = Depends(get_db), current_user: schemas.User = Depends(get_cred())
):
    return BoardRepo.get_user_boards(db, current_user.id)


@router.get("/{id}", response_model=schemas.BoardDetail)
def get_board_detail(id: str, db: Session = Depends(get_db)):
    return BoardRepo.get_by_id(db, id)


@router.post("/add-member")
def board_add_member(
    board_id: str,
    member_id: str,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_cred()),
):
    return BoardRepo.add_member(db, board_id, member_id, current_user.id)


@router.post("/", response_model=schemas.BoardDetail)
def create_board(
    req: schemas.Board,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_cred()),
):
    return BoardRepo.create(db, req, current_user.id)
