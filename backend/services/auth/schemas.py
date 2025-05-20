from pydantic import (
    BaseModel,
    EmailStr,
    Field,
)
from ...core.validators import password_pattern


class Login(BaseModel):
    user_email: EmailStr
    user_password: str = Field(pattern=password_pattern)


class AuthToken(BaseModel):
    auth_token: str


__all__ = (
    "Login",
    "AuthToken",
)
