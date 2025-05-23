from pydantic import BaseModel, EmailStr, Field

from ...core.validators import (
    username_pattern,
    display_name_pattern,
    email_pattern,
    password_pattern,
)


class GetUserSchema(BaseModel):
    user_id: int


class CreateUserSchema(BaseModel):
    username: str = Field(pattern=username_pattern)
    display_name: str | None = Field(pattern=display_name_pattern, default=None)
    password: str = Field(pattern=password_pattern)
    email: EmailStr = Field(pattern=email_pattern)


__all__ = (
    "GetUserSchema",
    "CreateUserSchema",
)
