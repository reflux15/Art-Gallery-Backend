import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routers.user_router import router as user_router
from routers.art_router import router as art_router
from utils.db import engine, Base


def create_app():
    app = FastAPI(docs_url="/")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(user_router)
    app.include_router(art_router)
    return app


if __name__ == "__main__":
    Base.metadata.create_all(
        bind=engine
    )  # creates all the tables, will not attempt to recreate if they exist
    uvicorn.run("main:create_app", host="localhost", port=8000, reload=True)