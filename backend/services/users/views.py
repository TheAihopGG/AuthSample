from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import (
    APIRouter,
    Depends,
    status,
)
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

from ...core.database_helper import database_helper
from ...core.configuration import DATETIME_FORMAT
from .crud import (
    create_user,
    get_user_by_id,
)
from .schemas import (
    GetUserSchema,
    CreateUserSchema,
)

router = APIRouter(prefix="/users", tags=["Users"])


@router.get(
    "/get_user_info",
    summary="Получает информацию о пользователе по user_id",
    description="Эндпоинт для получения пользователя",
)
async def get_user_endpoint(
    schema: GetUserSchema,
    session: AsyncSession = Depends(database_helper.session_dependency),
) -> JSONResponse:
    if user := await get_user_by_id(session, user_id=schema.user_id):
        return JSONResponse(
            {
                "id": user.id,
                "username": user.username,
                "display_name": user.display_name,
                "is_active": user.is_active,
                "created_at": user.created_at.strftime(DATETIME_FORMAT),
            }
        )
    else:
        return JSONResponse(
            {"detail": "user was not founded"},
            status_code=status.HTTP_404_NOT_FOUND,
        )


@router.post(
    "/create_user",
    summary="Создаёт пользователя",
    description="Эндпоинт для создания пользователя",
)
async def create_user_endpoint(
    schema: CreateUserSchema,
    session: AsyncSession = Depends(database_helper.session_dependency),
) -> JSONResponse:
    try:
        user = await create_user(
            session,
            username=schema.username,
            display_name=schema.display_name,
            email=schema.email,
            password=schema.password,
        )
    except IntegrityError as err:
        return JSONResponse(
            {
                "detail": "constraint conflict",
                "constraint_name": err.orig.diag.constraint_name,  # type: ignore
            },
            status_code=status.HTTP_409_CONFLICT,
        )
    else:
        return JSONResponse(
            {
                "id": user.id,
                "username": user.username,
                "display_name": user.display_name,
                "password_hash": user.password_hash,
                "email": user.email,
                "is_active": user.is_active,
                "created_at": user.created_at.strftime(DATETIME_FORMAT),
            },
            status_code=status.HTTP_201_CREATED,
        )
