from sqlalchemy import text, insert
from sqlalchemy.orm import Session

from models.orm.models import ArtPiece
from models.dto.models import CreateArt


class ArtRepo:
    def __init__(self, db: Session):
        self.db_session = db

    def get_art(self):      # get all art pieces
        return self.db_session.query(ArtPiece).all()

    def insert_art(self, art: CreateArt):
        statement = insert(ArtPiece).values(
            name=art.name,
            category=art.category,
            subject=art.subject,
            artist_name=art.artist_name,
            file_name=art.file_name,
        )
        self.db_session.execute(statement=statement)
        self.db_session.commit()
