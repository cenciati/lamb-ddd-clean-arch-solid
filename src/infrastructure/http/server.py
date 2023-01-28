from fastapi import FastAPI
from sqlalchemy.engine import Engine
from uvicorn import run

from src.infrastructure.database.sqlalchemy.db_connection_handler import (
    DBConnectionHandler,
)
from src.infrastructure.database.sqlalchemy.model.commentary_model import (
    Base as BaseCommentaries,
)
from src.infrastructure.database.sqlalchemy.model.customer_model import (
    Base as Basecustomers,
)
from src.infrastructure.database.sqlalchemy.model.user_model import Base as BaseUsers
from src.infrastructure.http.routes.customer_route import customer_router
from src.infrastructure.http.routes.extract_route import extract_router
from src.infrastructure.http.routes.root_route import root_router
from src.infrastructure.http.routes.user_route import user_router
from src.infrastructure.settings import Settings


def setup_database() -> None:
    """Starts the database, creates tables and configure them."""
    db_connection_handler = DBConnectionHandler()
    engine: Engine = db_connection_handler.get_engine()
    BaseCommentaries.metadata.create_all(bind=engine, checkfirst=True)
    Basecustomers.metadata.create_all(bind=engine, checkfirst=True)
    BaseUsers.metadata.create_all(bind=engine, checkfirst=True)


app = FastAPI(
    title="Lamb-extract",
    description="RESTful API to consume data from comments left by customers.",
    version="0.1.0",
    license_info={"name": "MIT"},
)
settings = Settings()
app.include_router(root_router, prefix=settings.API_V1_STR, tags=["root"])
app.include_router(extract_router, prefix=settings.API_V1_STR, tags=["extract"])
app.include_router(customer_router, prefix=settings.API_V1_STR, tags=["customers"])
app.include_router(user_router, prefix=settings.API_V1_STR, tags=["users"])

if __name__ == "__main__":
    setup_database()
    run(
        app="src.infrastructure.http.server:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="debug",
    )
