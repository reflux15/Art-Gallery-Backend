import enum

from sqlalchemy import (
    Column,
    Integer,
    String,
    Enum,
    func,
    DateTime,
    Boolean,
    ForeignKey,
    Date,
    Time,
    Interval,
    JSON, LargeBinary,
)
from sqlalchemy.dialects.postgresql import ENUM

from utils.db import Base

"""
relations: 
- User 1:1 ArtistProfile    # One user (artis) has 1 artist profile
- User 1:n Order            # One user can have many orders
- Order 1:1 ArtPiece        # One order can have 1 art piece inside of it
- User 1:n ArtPiece         # One user (artist) can be the author of many art pieces
- Favorites n:1 User        # One user can have many favorites
- Favorites n:1 ArtPiece    # One art piece can be added to favorites by multiple users
"""


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String(50), nullable=False)       # artist or buyer
    username = Column(String(50), nullable=False)   # must be unique
    password = Column(String(200), nullable=False)
    full_name = Column(String(200))
    email = Column(String(200))
    password_hash = Column(String(500), nullable=False)


class ArtPiece(Base):
    __tablename__ = "artPieces"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    category = Column(String(200), nullable=False)
    subject = Column(String(200), nullable=False)
    artist_name = Column(String(200), nullable=False)
    file_name = Column(String(200), nullable=False)


class ArtistProfile(Base):
    __tablename__ = "artistProfiles"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(1000))
    start_date = Column(DateTime)   # date the artist started making art
    image = Column(LargeBinary)     # image is stored as BYTEA column in postgres, only supports small resolution images


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    art_piece_id = Column(Integer, ForeignKey("artPieces.id"))
    status = Column(String(50))
    estimated_delivery = Column(DateTime)


class Favorites(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))           # the user who added the art piece to favorites
    art_piece_id = Column(Integer, ForeignKey("artPieces.id"))  # the art piece added to favorites
