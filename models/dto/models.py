from pydantic import BaseModel


# model used by the register user endpoint
class UserRegister(BaseModel):
    username: str
    password: str
    role: str = "buyer"
    full_name: str
    email: str


# model used by the login user endpoint
class UserLogin(BaseModel):
    username: str  # usernames are unique across users
    password: str
    role: str = "buyer"


# model returned by endpoints which create data
class GenericResponse(BaseModel):
    message: str


