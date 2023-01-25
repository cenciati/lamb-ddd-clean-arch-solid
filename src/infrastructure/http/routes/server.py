from fastapi import FastAPI

from src.infrastructure.http.routes.customer_route import customer_router
from src.infrastructure.http.routes.root_route import root_router
from src.infrastructure.settings import Settings

settings = Settings()
app = FastAPI(
    title="Lamb-extract",
    description="RESTful API to consume data about comments left by customers.",
    version="0.1.0",
    license_info={"name": "MIT"},
)

app.include_router(root_router, prefix=settings.API_V1_STR, tags=["root"])
# app.include_router(extract_router, prefix=settings.API_V1_STR, tags=["extract"])
app.include_router(customer_router, prefix=settings.API_V1_STR, tags=["customers"])
# app.include_router(users_router, prefix=settings.API_V1_STR, tags=["users"])
