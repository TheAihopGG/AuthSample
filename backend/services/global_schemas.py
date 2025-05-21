from pydantic import BaseModel


class DetailSchema(BaseModel):
    detail: str


__all__ = ("DetailSchema",)
