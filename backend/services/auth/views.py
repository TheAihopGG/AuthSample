from fastapi import (
    APIRouter,
    Depends,
    status,
)
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from .dependencies import user_authorization_from_auth_token_dependency
from ...core.models import User
from ...core.database_helper import database_helper
from ..users.crud import get_user_by_email
from .crud import (
    encode_auth_token,
    authenticate_user,
)
from .schemas import LoginSchema

router = APIRouter(prefix="/auth", tags=["Users"])


@router.post(
    "/signin",
    summary="Возвращает auth_token",
    description="Эндпоинт для авторизации",
)
async def signin_endpoint(
    schema: LoginSchema,
    session: AsyncSession = Depends(database_helper.session_dependency),
):
    if user := await get_user_by_email(
        session,
        email=schema.user_email,
    ):
        if authenticate_user(
            user,
            user_email=schema.user_email,
            user_password=schema.user_password,
        ):
            return JSONResponse({"auth_token": encode_auth_token(user_id=user.id)})
        else:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "invalid email or password"},
            )


@router.post(
    "/authorize",
    summary="Принимает auth_token и проверяет его",
    description="Эндпоинт для тестирования системы авторизации",
)
async def authorize_endpoint(
    user: User = Depends(user_authorization_from_auth_token_dependency),
):
    return JSONResponse({"detail": f"you have authorized as {user.username}"})
