from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import (
    select,
    update,
    delete,
)

from ...core.utils import (
    log_function_call,
    hash_password,
)
from ...core.database_helper import database_helper
from ...core.models import User
from ...core.errors import InvalidValueError
from ...core.validators import (
    is_valid_display_name,
    is_valid_username,
    is_valid_password,
    is_valid_email,
)


@log_function_call()
async def create_user(
    session: AsyncSession,
    *,
    username: str,
    password: str,
    email: str,
    display_name: str | None = None,
) -> User:
    username = username.lower()
    if not display_name:
        display_name = username

    # if not is_valid_username(username):
    #     raise InvalidValueError("username", username)
    # if not is_valid_display_name(display_name):
    #     raise InvalidValueError("display_name", display_name)
    # if not is_valid_email(email):
    #     raise InvalidValueError("email", email)
    # if not is_valid_password(email):
    #     raise InvalidValueError("password", password)

    user = User(
        username=username,
        password_hash=hash_password(password),
        email=email,
        display_name=display_name,
    )
    session.add(user)
    await session.commit()

    return user


@log_function_call()
async def toggle_user_active_by_id(
    session: AsyncSession,
    *,
    user_id: int,
    is_active: bool,
) -> bool:
    result = await session.execute(
        update(
            User,
        )
        .where(
            User.id == user_id,
        )
        .values(
            is_active=is_active,
        )
    )
    await session.commit()

    return bool(result.rowcount)


@log_function_call()
async def delete_user_by_id(session: AsyncSession, *, user_id: int) -> bool:
    result = await session.execute(
        delete(
            User,
        ).where(
            User.id == user_id,
        ),
    )
    await session.commit()

    return bool(result.rowcount)


@log_function_call()
async def get_user_by_id(session: AsyncSession, *, user_id: int) -> User | None:
    return await session.get(User, user_id)


@log_function_call()
async def update_user_by_id(
    session: AsyncSession,
    user_id: int,
    **kwargs,
) -> bool:
    result = await session.execute(
        update(
            User,
        )
        .where(
            User.id == user_id,
        )
        .values(
            **kwargs,
        )
    )
    return bool(result.rowcount)


__all__ = (
    "create_user",
    "update_user_by_id",
    "delete_user_by_id",
    "toggle_user_active_by_id",
    "get_user_by_id",
)
