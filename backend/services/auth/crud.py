from datetime import datetime, timedelta, timezone
from jwt import (
    JWT,
    jwk_from_pem,
)
from jwt.utils import get_int_from_datetime

from ...core.configuration import (
    AUTH_PRIVATE_KEY_PATH,
    AUTH_JWT_ALGORITHM,
    AUTH_TOKEN_LIFETIME,
)

jwt = JWT()


def encode_auth_token(
    payload: dict,
    private_key: bytes = open(AUTH_PRIVATE_KEY_PATH, "rb").read(),
    algorithm: str = AUTH_JWT_ALGORITHM,
    lifetime: timedelta = AUTH_TOKEN_LIFETIME,
) -> str:
    payload.update(
        {
            "created_at": get_int_from_datetime(datetime.now()),
            "expires_at": get_int_from_datetime(datetime.now() + lifetime),
        }
    )
    return jwt.encode(payload, key=jwk_from_pem(private_key), alg=algorithm)


def decode_auth_token(
    auth_token: str,
    public_key: bytes = open(AUTH_PRIVATE_KEY_PATH, "rb").read(),
):
    return jwt.decode(
        auth_token, key=jwk_from_pem(public_key), algorithms={AUTH_JWT_ALGORITHM}
    )


__all__ = (
    "encode_auth_token",
    "decode_auth_token",
)
