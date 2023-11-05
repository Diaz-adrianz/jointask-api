import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import db.tables
from config import config, is_dev

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", config["CLIENT_URL"]],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    host = str(config["HOST"])
    port = int(str(config["PORT"]))

    uvicorn.run(
        app="main:app",
        host=host,
        port=port,
        reload=is_dev(),
    )
