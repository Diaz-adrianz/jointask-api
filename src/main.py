import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

import db.tables
from config import config, is_dev

from core.user import route as UserRoute
from core.board import route as BoardRoute
from core.auth import auth

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", config["CLIENT_URL"]],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(UserRoute.router)
app.include_router(BoardRoute.router)


if __name__ == "__main__":
    host = str(config["HOST"])
    port = int(str(config["PORT"]))

    uvicorn.run(
        app="main:app",
        host=host,
        port=port,
        reload=is_dev(),
    )
