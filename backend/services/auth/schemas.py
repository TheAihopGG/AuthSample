from pydantic import (
    BaseModel,
    EmailStr,
    Field,
)
from ...core.validators import password_pattern


class LoginSchema(BaseModel):
    user_email: EmailStr
    user_password: str = Field(pattern=password_pattern)


class AuthTokenSchema(BaseModel):
    auth_token: str


__all__ = (
    "LoginSchema",
    "AuthTokenSchema",
)
