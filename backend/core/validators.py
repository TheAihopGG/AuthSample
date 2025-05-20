import re
from functools import cache

username_pattern = r"^[a-z0-9_]{1,32}$"
display_name_pattern = r"^[A-Za-zА-Яа-яЁё0-9_]{1,32}$"
password_pattern = r"^[A-Za-z0-9_]{1,32}$"
email_pattern = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+$"


@cache
def is_valid_username(username: str) -> re.Match | None:
    return re.search(username_pattern, username)


@cache
def is_valid_display_name(display_name: str) -> re.Match | None:
    return re.search(display_name_pattern, display_name)


@cache
def is_valid_password(password: str) -> re.Match | None:
    return re.search(password_pattern, password)


@cache
def is_valid_email(email: str) -> re.Match | None:
    return re.search(email_pattern, email)


__all__ = (
    "is_valid_username",
    "is_valid_display_name",
    "is_valid_password",
    "is_valid_email",
    "username_pattern",
    "display_name_pattern",
    "password_pattern",
    "email_pattern",
)
