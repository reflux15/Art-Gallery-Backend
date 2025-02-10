import secrets

from fastapi import APIRouter, Depends, UploadFile
from fastapi.security import HTTPBasic
from starlette.responses import FileResponse

from repository.art_repo import ArtRepo
from utils.db import get_db

router = APIRouter(prefix="/art", tags=["art"])
security = HTTPBasic()


def art_repository(db=Depends(get_db)):
    return ArtRepo(db=db)

@router.get("/image/{id}")
async def get_metadata(id: str, db: ArtRepo = Depends(art_repository)):
    pass

@router.post("/image/{id}")
async def create_metadata(id: str, db: ArtRepo = Depends(art_repository)):
    pass


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
