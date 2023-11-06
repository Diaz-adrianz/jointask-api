import uuid
from fastapi import HTTPException
from sqlalchemy import UUID, cast
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import IntegrityError
from utils.hash import Hash
from core.board import model as model_board
from . import model
from . import schema


class UserRepo:
    def create(db: Session, req: schema.User):
        new_user = model.User(
            name=req.name, email=req.email, password=Hash.bcrypt(req.password)
        )

        try:
            db.add(new_user)
            db.commit()
            db.refresh(new_user)

            return new_user

        except IntegrityError as e:
            db.rollback()

            if 'unique constraint "users_email_key"' in str(e):
                raise HTTPException(status_code=403, detail="Email already exist")

    def update(db: Session, id: int, req: schema.User):
        user = db.query(model.User).filter(model.User.id == id)
        user.update(
            {
                model.User.name: req.name,
            }
        )

        try:
            db.commit()
            # db.refresh(model)
            return model.first()

        except IntegrityError as e:
            db.rollback()

            print(e)
            raise HTTPException(status_code=500, detail="Internal server error")

    def get_user_boards(db: Session, id: str):
        owned_boards = (
            db.query(model_board.Board).filter(model_board.Board.owner_id == id).all()
        )

        return schema.UserBoards(owned_boards=owned_boards)

    def get_user_by_id(db: Session, id: str):
        user = db.query(model.User).filter(model.User.id == (id)).first()

        if not user:
            raise HTTPException(status_code=404, detail=f"User with Id {id} not found")
        return user
