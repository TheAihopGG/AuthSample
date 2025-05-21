from datetime import datetime
from fastapi import Header, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ...services.auth.crud import decode_auth_token
from ...core.database_helper import database_helper
from ...core.models import User
from ..users.crud import get_user_by_id


async def user_identification_from_auth_token_dependency(
    auth_token: str = Header(alias="Authorization"),
    session: AsyncSession = Depends(database_helper.session_dependency),
) -> User:
    """
    Получает auth_token из заголовка Authorization, извлекает из него user_id и находит по нему пользователя.
    """
    if auth_token_payload := decode_auth_token(auth_token):
        if user_id := auth_token_payload.get("user_id"):
            if expires_at := auth_token_payload.get("expires_at"):
                if expires_at > datetime.now().timestamp():
                    if user := await get_user_by_id(session, user_id=user_id):
                        return user
                    else:
                        raise HTTPException(
                            status_code=status.HTTP_404_NOT_FOUND,
                            detail="user was not founded",
                        )
                else:
                    raise HTTPException(
                        status_code=status.HTTP_403_FORBIDDEN,
                        detail="token expired",
                    )
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="invalid auth token",
    )


async def user_authorization_from_auth_token_dependency(
    user: User = Depends(user_identification_from_auth_token_dependency),
):
    """Проверяет права пользователя"""
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="user is not active",
        )
    return user


__all__ = (
    "user_identification_from_auth_token_dependency",
    "user_authorization_from_auth_token_dependency",
)
