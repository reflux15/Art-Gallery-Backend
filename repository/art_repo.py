from sqlalchemy import text, insert
from sqlalchemy.orm import Session

from models.orm.models import ArtPiece
from models.dto.models import CreateArt


class ArtRepo:
    def __init__(self, db: Session):
        self.db_session = db

    def get_art(self):      # get all art pieces
        return self.db_session.query(ArtPiece)

    def get_art_by_author(self, author_id):
        return self.db_session.query(ArtPiece).filter(ArtPiece.author_id == author_id).all()

    def insert_art(self, art: CreateArt):
        statement = insert(ArtPiece).values(
            title=art.title,
            author_id=art.author_id,
            description=art.description,
            creation_date=art.creation_date,
            price=art.price,
            currency=art.currency,
            image=art.image,
            category=art.category,
            type=art.type,
        )
        self.db_session.execute(statement=statement)
        self.db_session.commit()
