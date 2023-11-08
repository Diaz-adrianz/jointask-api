from fastapi import HTTPException
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import IntegrityError

from core.user.repo import UserRepo

from . import model
from .member import model as model_member
from core import schemas


class BoardRepo:
    def get_all(db: Session):
        return db.query(model.Board).all()

    def get_by_id(db: Session, id: str) -> schemas.BoardDetail:
        board = db.query(model.Board).filter(model.Board.id == (id)).first()

        if not board:
            raise HTTPException(status_code=404, detail=f"Board with Id {id} not found")

        return board

    def get_user_boards(db: Session, id: str):
        owned_boards = db.query(model.Board).filter(model.Board.owner_id == id).all()
        joined_boards = (
            db.query(model.Board).filter(model.Board.members.any(user_id=id)).all()
        )

        return schemas.UserBoards(
            owned_boards=[schemas.Board(**board.__dict__) for board in owned_boards],
            joined_boards=[schemas.Board(**board.__dict__) for board in joined_boards],
        )

    def add_member(db: Session, board_id: str, member_id: str, user_id: str):
        user = UserRepo.get_user_by_id(db, member_id)
        board = BoardRepo.get_by_id(db, board_id)

        if board.owner_id != user_id:
            raise HTTPException(status_code=403, detail="You dont have permission")

        new_member = model_member.BoardMember(user_id=user.id, board_id=board_id)

        try:
            db.add(new_member)
            db.commit()

            return {"detail": "New member added successfully"}

        except IntegrityError as e:
            db.rollback()

            print(e)
            raise HTTPException(status_code=500, detail="Internal server error")

    def is_user_have_acces(db: Session, board_id: str, user_id: str):
        board: schemas.BoardDetail = BoardRepo.get_by_id(db, board_id)

        is_accepted = (board.owner_id == user_id) or any(
            member.user_id == user_id for member in board.members
        )

        if not is_accepted:
            raise HTTPException(
                status_code=403, detail="You dont have access to the board"
            )
        else:
            return True

    def create(db: Session, req: schemas.Board, owner_id: str):
        new_board = model.Board(
            title=req.title, description=req.description, owner_id=owner_id
        )

        try:
            db.add(new_board)
            db.commit()
            db.refresh(new_board)

            return new_board

        except IntegrityError as e:
            db.rollback()

            raise HTTPException(status_code=500, detail="Internal server error")
