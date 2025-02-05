from sqlalchemy import text, insert
from sqlalchemy.orm import Session

from models.orm.models import User
from models.dto.models import UserRegister


class UserRepo:
    def __init__(self, db: Session):
        self.db_session = db

    def get_users(self):
        return self.db_session.query(User).all()

    def get_users_by_role(self, role):
        return self.db_session.query(User).filter(User.role == role).all()

    def get_users_by_username(self, username):
        return self.db_session.query(User).filter(User.username == username).first()

    def get_user_by_id(self, user_id):  # user id is uniques so this query should return a single element always
        return self.db_session.query(User).filter(User.id == user_id).first()

    def insert_user(self, user: UserRegister):
        statement = insert(User).values(
            role=user.role,
            username=user.username,
            password=user.password,
            full_name=user.full_name,
            email=user.email,
            password_hash=user.password
        )
        self.db_session.execute(statement=statement)
        self.db_session.commit()

