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
    JSON,
)
from sqlalchemy.dialects.postgresql import ENUM

from utils.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String(50))       # artist or buyer
    username = Column(String(50))   # must be unique
    password = Column(String(200))
    full_name = Column(String(50))
    email = Column(String(50))
    password_hash = Column(String(50))