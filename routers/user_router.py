from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.responses import JSONResponse

from models.dto.models import GenericResponse, UserRegister
from repository.user_repo import UserRepo
from utils.db import get_db

router = APIRouter(prefix="/users", tags=["users"])
security = HTTPBasic()


# dependency injected in every endpoint handler to facilitate interaction with database
def users_repository(db=Depends(get_db)):
    return UserRepo(db=db)


@router.get("/")
def get_users(db: UserRepo = Depends(users_repository)):
    users_from_db = db.get_users()
    users_result = []
    for user in users_from_db:
        users_result.append({"id": user.id, "full_name": user.full_name, "email": user.email})
    return users_result


@router.post("/register", response_model=GenericResponse)
def register_user(user: UserRegister, db: UserRepo = Depends(users_repository)):
    # see if a user with the same username already exists
    existing_user = db.get_user_by_username(user.username)
    if existing_user:
        return JSONResponse(
            status_code=400,
            content=jsonable_encoder(
                GenericResponse(message="User with email or username already registered for given role.")),
        )
    db.insert_user(user)
    return JSONResponse(
        status_code=201,
        content=jsonable_encoder(
            GenericResponse(message="User registered successfully.")),
    )


def authenticate_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)],
                      db: UserRepo = Depends(users_repository)):
    """Authenticate user using Basic Auth."""
    user = db.get_user_by_username(credentials.username)
    if not user or not user.password == credentials.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return user


@router.post("/login")
def login(user: Annotated[dict, Depends(authenticate_user)]):
    """Login endpoint using Basic Authentication without JWT."""
    return {"message": "Login successful", "user_id": user.id, "username": user.username, "role": user.role}
