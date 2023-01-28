from typing import Dict

from fastapi import APIRouter, status

root_router = APIRouter()


@root_router.get("/", status_code=status.HTTP_200_OK, response_model=Dict[str, list])
def root():
    return {"data": [{"Go to:": "/extract"}]}
