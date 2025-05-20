import bcrypt
from logging import getLogger
from typing import Awaitable, Callable

from .configuration import APP_ECHO

logger = getLogger(__name__)


def log_function_call[**P, R](
    echo: bool = APP_ECHO,
) -> Callable[[Callable[P, Awaitable[R]]], Callable[P, Awaitable[R]]]:
    def inner[**P2, R2](
        func: Callable[P2, Awaitable[R2]],
    ) -> Callable[P2, Awaitable[R2]]:
        async def wrapper(*args: P2.args, **kwargs: P2.kwargs) -> R2:
            if echo:
                logger.info(f"{func.__name__}({args},{kwargs})")
            return await func(*args, **kwargs)

        return wrapper

    return inner


def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


__all__ = ("log_function_call",)
