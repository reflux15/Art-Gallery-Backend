import secrets

from fastapi import APIRouter, Depends, UploadFile
from fastapi.security import HTTPBasic
from sqlalchemy import insert
from starlette.responses import FileResponse

from models.dto.models import CreateArt
from models.orm.models import ArtPiece
from repository.art_repo import ArtRepo
from utils.db import get_db

router = APIRouter(prefix="/art", tags=["art"])
security = HTTPBasic()


def art_repository(db=Depends(get_db)):
    return ArtRepo(db=db)


@router.get("/image/")
async def get_art(db: ArtRepo = Depends(art_repository)):
    art =  db.get_art()
    return art


@router.post("/image/")
async def create_metadata(data: CreateArt, db: ArtRepo = Depends(art_repository)):
    db.insert_art(data)
    return {
        "ok": True
    }


@router.get("/upload/{id}/")
async def get_image(id: str):
    return FileResponse(path=f"./uploads/{id}.png")


@router.post("/upload")
async def upload_image(file: UploadFile):
    filename = secrets.token_hex(nbytes=16)
    data = await file.read()
    with open(f"./uploads/{filename}.png", "wb") as f:
        f.write(data)
    return {
        "filename": f"{filename}.png",
    }
