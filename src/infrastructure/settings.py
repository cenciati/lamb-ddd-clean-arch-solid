import logging
from typing import Optional

from pydantic import BaseSettings, Field


class LoggingSettings(BaseSettings):
    """Settings for logging"""

    LOGGING_LEVEL: int = logging.INFO


class DBSettings(BaseSettings):
    """Database settings and environment variables."""

    DB_DRIVER: Optional[str] = Field(..., env="DB_DRIVER")
    DB_USER: Optional[str] = Field(..., env="DB_USER")
    DB_PASSWORD: Optional[str] = Field(..., env="DB_PASSWORD")
    DB_HOST: Optional[str] = Field(..., env="DB_HOST")
    DB_PORT: Optional[str] = Field(..., env="DB_PORT")
    DB_NAME: Optional[str] = Field(..., env="DB_NAME")
    SQLALCHEMY_DATABASE_URI: str = (
        f"{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


class Settings(BaseSettings):
    """Project general settings."""

    API_V1_STR: str = "/api/v1"
    BASE_URL: str = f"http://localhost:8000{API_V1_STR}"
    db: DBSettings = DBSettings()
    logging: LoggingSettings = LoggingSettings()

    class Config:
        """Set default parameters."""

        case_sensitive: bool = True
        env_file: str = ".env"
