from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from sqlalchemy import func
from datetime import datetime

from .base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    """User unique id"""
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    """Unique user name"""
    display_name: Mapped[str] = mapped_column(nullable=False, default=username)
    """Display name can be different from username and not unique"""
    password_hash: Mapped[bytes] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(nullable=False, default=True)
    """If user is inactivate actions from this account and disabled"""

    created_at: Mapped[datetime] = mapped_column(
        nullable=False,
        default=datetime.now,
        server_default=func.now(),
    )


__all__ = ("User",)
