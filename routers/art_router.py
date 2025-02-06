from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasic

from repository.art_repo import ArtRepo
from utils.db import get_db

router = APIRouter(prefix="/art", tags=["art"])
security = HTTPBasic()


def art_repository(db=Depends(get_db)):
    return ArtRepo(db=db)


