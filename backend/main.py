import logging
from typing import Callable
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager

from .services import (
    users,
    auth,
)

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename="./backend/logs.log",
    encoding="utf-8",
    level=logging.DEBUG,
    filemode="w",
    format="%(levelname)s:\t%(message)s (%(asctime)s)",
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.debug("Application startup complete.")
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(users.router)
app.include_router(auth.router)


@app.middleware("http")
async def middleware(request: Request, call_next: Callable):
    logger.debug(f"{request.method.upper()} {request.url}")
    return await call_next(request)
