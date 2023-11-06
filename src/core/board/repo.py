from fastapi import HTTPException
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import IntegrityError

from . import schema, model


class BoardRepo:
    def get_all(db: Session):
        return db.query(model.Board).all()

    def get_by_id(db: Session, id: str):
        board = db.query(model.Board).filter(model.Board.id == (id)).first()

        if not board:
            raise HTTPException(status_code=404, detail=f"Board with Id {id} not found")

        return board

    def create(db: Session, req: schema.Board, owner_id: str):
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

    def update(db: Session, id: str):
        pass
