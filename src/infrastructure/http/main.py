from sqlalchemy.engine import Engine
from uvicorn import run

from src.infrastructure.database.sqlalchemy.db_config import Base
from src.infrastructure.database.sqlalchemy.db_connection_handler import (
    DBConnectionHandler,
)


def setup_database() -> None:
    """Starts the database, creates tables and configure them."""
    engine: Engine = DBConnectionHandler().get_engine()
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    # setup_database()
    run(
        app="src.infrastructure.http.routes.server:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="debug",
    )
