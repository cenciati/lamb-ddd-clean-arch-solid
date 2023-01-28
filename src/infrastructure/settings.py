from logging import INFO
from os import getenv
from typing import Optional

from dotenv import find_dotenv, load_dotenv
from pydantic import BaseSettings

load_dotenv(find_dotenv())


class LoggingSettings(BaseSettings):
    """Settings for logging"""

    LOGGING_LEVEL: int = INFO


class DBSettings(BaseSettings):
    """Database settings, including the credentials."""

    DB_DRIVER: Optional[str] = getenv("DB_DRIVER")
    DB_USER: Optional[str] = getenv("DB_USER")
    DB_PASSWORD: Optional[str] = getenv("DB_PASSWORD")
    DB_HOST: Optional[str] = getenv("DB_HOST")
    DB_PORT: Optional[str] = getenv("DB_PORT")
    DB_NAME: Optional[str] = getenv("DB_NAME")
    SQLALCHEMY_DATABASE_URI: str = (
        f"{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


class Settings(BaseSettings):
    """Project general settings."""

    API_V1_STR: str = "/api/v1"
    URL: str = "http://localhost:8000"
    BASE_URL: str = f"{URL}{API_V1_STR}"
    db: DBSettings = DBSettings()
    log: LoggingSettings = LoggingSettings()

    def get_db_connection_string(self) -> str:
        return self.db.SQLALCHEMY_DATABASE_URI

    class Config:
        """Set default parameters."""

        case_sensitive: bool = True
        env_file: str = ".env"
