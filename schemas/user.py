from pydantic import BaseModel,EmailStr, Field
from enum import Enum

class UserStatus(str, Enum):
    active = "active"
    inactive = "inactive"
    suspended = "suspended"
    pending = "pending"

class UserCreate(BaseModel):
    user_name: str
    email: EmailStr
    password: str = Field(..., min_length=4)
    status: UserStatus


# Properties required for user update
class UserUpdate(BaseModel):
    email: EmailStr
    user_name: str
    status: str
    image: str
    updated_at: str
    status: UserStatus


# Properties returned in the response for a single user
class UserResponse(BaseModel):
    user_id: int
    email: EmailStr
    user_name: str
    status: str
    image: str
    status: UserStatus
    

    class Config:
        orm_mode = True


# Properties returned in the response for user list
class UserListResponse(BaseModel):
    users: list[UserResponse]


# Properties required during user authentication (login)
class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=4)


# Properties returned in the response after successful authentication (login)
class UserLoginResponse(BaseModel):
    access_token: str
    refresh_token:str
    token_type: str


# Properties required to reset the user password
class UserPasswordReset(BaseModel):
    email: EmailStr
    new_password: str = Field(..., min_length=4)
