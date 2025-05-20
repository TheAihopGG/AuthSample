from os import getenv
from dotenv import load_dotenv
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

assert load_dotenv(BASE_DIR / ".env"), f"{BASE_DIR / '.env'} does not exists"

DATABASE_HOST = "localhost"
DATABASE_PORT = 5432
DATABASE_PASSWORD = str(getenv("DATABASE_PASSWORD"))
DATABASE_USER_NAME = "postgres"
DATABASE_NAME = "auth_sample"
DATABASE_ECHO = True
DATABASE_URL = f"postgresql+psycopg://{DATABASE_USER_NAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

APP_HOST = "localhost"
APP_PORT = 8000
APP_PATH = "backend.main:app"
APP_ECHO = True

AUTH_PRIVATE_KEY_PATH = BASE_DIR / "services/auth/certs/private_key.pem"
AUTH_PUBLIC_KEY_PATH = BASE_DIR / "services/auth/certs/public_key.pem"
AUTH_JWT_ALGORITHM = "RS256"
AUTH_TOKEN_LIFETIME = timedelta(weeks=4)

DATETIME_FORMAT = "%d/%m/%Y, %H:%M:%S"
