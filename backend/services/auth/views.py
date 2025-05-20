import bcrypt
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import timedelta, datetime
from fastapi import (
    APIRouter,
    Depends,
    status,
    Header,
)
from fastapi.responses import JSONResponse, Response

from ...core.models import User
from .dependencies import get_user_by_auth_token_dependency
from .schemas import AuthToken, Login
from ...core.database_helper import database_helper
from .crud import (
    decode_auth_token,
    encode_auth_token,
)
from ..users.crud import (
    get_user_by_email,
    get_user_by_id,
)

router = APIRouter(prefix="/auth", tags=["Users"])


@router.post("/login")
async def login_endpoint(
    response: Response,
    schema: Login,
    session: AsyncSession = Depends(database_helper.session_dependency),
):
    if user := await get_user_by_email(
        session,
        email=schema.user_email,
    ):
        if bcrypt.checkpw(schema.user_password.encode("utf"), user.password_hash):
            return JSONResponse(
                {"auth_token": encode_auth_token(user_id=user.id)},
                status_code=status.HTTP_202_ACCEPTED,
            )
        else:
            return JSONResponse(
                {"detail": "incorrect password or email"},
                status_code=status.HTTP_403_FORBIDDEN,
            )
    else:
        return JSONResponse(
            {"detail": "user was not founded"},
            status_code=status.HTTP_404_NOT_FOUND,
        )


@router.post("/me")
async def get_me_endpoint(user: User = Depends(get_user_by_auth_token_dependency)):
    return JSONResponse(
        {"detail": f"Your password hash is {user.password_hash!r}"},
        status_code=status.HTTP_200_OK,
    )
