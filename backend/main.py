from logging import getLogger
from fastapi import FastAPI
from contextlib import asynccontextmanager

from .services import users
from .services.users.crud import create_user
from .core.database_helper import database_helper

logger = getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(users.router)
