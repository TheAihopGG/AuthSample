from typing import Any


class BaseError(Exception):
    pass


class InvalidValueError(BaseError):
    def __init__(self, var_name: str, var_value: Any):
        self.var_name: str = var_name
        self.var_value: Any = var_value


__all__ = (
    "BaseError",
    "InvalidValueError",
)
