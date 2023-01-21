# pylint: disable=attribute-defined-outside-init
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker

from src.infrastructure.settings import Settings

settings = Settings()


class DBConnectionHandler:
    """SQLAlchemy database connection helper."""

    def __init__(self) -> None:
        self.__connection_string: str = settings.get_db_connection_string()
        self.__engine: Engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self) -> Engine:
        """Creates a connection engine using the provided database
            connection string.
        Returns:
            A new connection engine object.
        """
        return create_engine(self.__connection_string)

    def get_engine(self) -> Engine:
        """Retrieves a created engine."""
        return self.__engine

    def __enter__(self):
        """Creates a new database session when entering the context.
        Returns:
            Database current context.
        """
        session_maker = sessionmaker()
        self.session = session_maker(
            autocommit=False, autoflush=False, bind=self.__engine
        )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close the database session when exiting the context."""
        self.session.close()  # type: ignore
