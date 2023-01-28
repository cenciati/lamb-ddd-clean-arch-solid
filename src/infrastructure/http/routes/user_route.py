from typing import Any, Dict, List, Optional, Sequence

from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from loguru import logger
from pydantic import EmailStr

from src.application.use_case.user.add.add_user import AddUserUseCase
from src.application.use_case.user.add.add_user_dto import (
    InputAddUserDTO,
    OutputAddUserDTO,
)
from src.application.use_case.user.delete.delete_user import DeleteUserUseCase
from src.application.use_case.user.delete.delete_user_dto import InputDeleteUserDTO
from src.application.use_case.user.find.find_all_users import FindAllUsersUseCase
from src.application.use_case.user.find.find_user_by_email import FindUserByEmailUseCase
from src.application.use_case.user.find.find_user_by_id import FindUserByIDUseCase
from src.application.use_case.user.find.find_user_dto import (
    InputFindUserByEmailDTO,
    InputFindUserByIDDTO,
    OutputFindUserDTO,
)
from src.application.use_case.user.update.update_user import UpdateUserUseCase
from src.application.use_case.user.update.update_user_dto import InputUpdateUserDTO
from src.domain.error.user_exception import (
    UserDuplicateEmailError,
    UserNotFoundError,
    UsersNotFoundError,
)
from src.infrastructure.presentation.data.user_presenter import UserPresenter
from src.infrastructure.presentation.error.user_exception_presentation import (
    ErrorMessageUserNotFound,
    ErrorMessageUsersNotFound,
)
from src.infrastructure.repository.memory.user_memory_repository import (
    UserInMemoryRepository,
)

user_router = APIRouter(prefix="/users")
repository = UserInMemoryRepository()
logger.add(
    "./reports/logs/api_users_{time}",
    format="{time} | {level} | {message} | {file}",
    colorize=True,
)


@user_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=Dict[str, Sequence[Dict[str, Any]]],
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorMessageUsersNotFound}},
)
def find_all_users():
    try:
        use_case = FindAllUsersUseCase(repository)
        found_users: Optional[Sequence[OutputFindUserDTO]] = use_case.execute()
        response = UserPresenter().to_json(found_users)
        return {"data": jsonable_encoder(response)}
    except UsersNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=exc.message
        ) from exc
    except Exception as exc:
        logger.error("Users could not be found.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        ) from exc


@user_router.get(
    "/id/{user_id}/",
    status_code=status.HTTP_200_OK,
    response_model=Dict[str, List[Dict[str, Any]]],
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorMessageUserNotFound}},
)
def find_user_by_id(user_id: str):
    try:
        use_case = FindUserByIDUseCase(repository)
        data = InputFindUserByIDDTO(id=user_id)
        found_user: Optional[OutputFindUserDTO] = use_case.execute(data)
        response = UserPresenter().to_json(found_user)
        return {"data": jsonable_encoder(response)}
    except UserNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=exc.message
        ) from exc
    except Exception as exc:
        logger.error("User could not be found by ID.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        ) from exc


@user_router.get(
    "/email/{user_email}/",
    status_code=status.HTTP_200_OK,
    response_model=Dict[str, List[Dict[str, Any]]],
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorMessageUserNotFound}},
)
def find_userary_by_email(user_email: EmailStr):
    try:
        use_case = FindUserByEmailUseCase(repository)
        data = InputFindUserByEmailDTO(email=user_email)
        found_users: Optional[OutputFindUserDTO] = use_case.execute(data)
        response = UserPresenter().to_json(found_users)
        return {"data": jsonable_encoder(response)}
    except UserNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=exc.message
        ) from exc
    except Exception as exc:
        logger.error("Users could not be found by e-mail.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        ) from exc


@user_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=Dict[str, List[Dict[str, Any]]],
)
def add_new_user(new_user: InputAddUserDTO):
    try:
        use_case = AddUserUseCase(repository)
        added_user: OutputAddUserDTO = use_case.execute(new_user)
        response = UserPresenter().to_json(added_user)
        return {"data": jsonable_encoder(response)}
    except UserDuplicateEmailError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=exc.message
        ) from exc
    except Exception as exc:
        logger.error("User could not be added.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        ) from exc


@user_router.put(
    "/{user_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None,
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorMessageUserNotFound}},
)
def update_user(updated_user: InputUpdateUserDTO):
    try:
        use_case = UpdateUserUseCase(repository)
        use_case.execute(updated_user)
    except UserNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=exc.message
        ) from exc
    except Exception as exc:
        logger.error("User could not be updated.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        ) from exc


@user_router.delete(
    "/{user_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None,
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorMessageUserNotFound}},
)
def delete_user_by_id(user_id: str):
    try:
        use_case = DeleteUserUseCase(repository)
        data = InputDeleteUserDTO(id=user_id)
        use_case.execute(data)
    except UserNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=exc.message
        ) from exc
    except Exception as exc:
        logger.error("User could not be deleted.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        ) from exc
