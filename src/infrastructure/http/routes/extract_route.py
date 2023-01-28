# pylint: disable=line-too-long
from typing import Any, Dict, List, Optional, Sequence

from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from loguru import logger

from src.application.use_case.commentary.add.add_commentary import AddCommentaryUseCase
from src.application.use_case.commentary.add.add_commentary_dto import (
    InputAddCommentaryDTO,
    OutputAddCommentaryDTO,
)
from src.application.use_case.commentary.delete.delete_commentary import (
    DeleteCommentaryUseCase,
)
from src.application.use_case.commentary.delete.delete_commentary_dto import (
    InputDeleteCommentaryDTO,
)
from src.application.use_case.commentary.find.find_all_commentaries import (
    FindAllCommentariesUseCase,
)
from src.application.use_case.commentary.find.find_commentaries_by_instance_slug import (  # noqa
    FindCommentariesByInstanceSlugUseCase,
)
from src.application.use_case.commentary.find.find_commentary_by_id import (
    FindCommentaryByIDUseCase,
)
from src.application.use_case.commentary.find.find_commentary_dto import (
    InputFindCommentaryByIDDTO,
    InputFindCommentaryByInstanceSlugDTO,
    OutputFindCommentaryDTO,
)
from src.domain.error.commentary_exception import (
    CommentariesNotFoundError,
    CommentaryNotFoundError,
)
from src.infrastructure.presentation.data.commentary_presenter import (
    CommentaryPresenter,
)
from src.infrastructure.presentation.error.commentary_exception_presentation import (
    ErrorMessageCommentariesNotFound,
    ErrorMessageCommentaryNotFound,
)
from src.infrastructure.repository.memory.commentary_memory_repository import (
    CommentaryInMemoryRepository,
)

extract_router = APIRouter(prefix="/extract")
repository = CommentaryInMemoryRepository()
logger.add(
    "./reports/logs/api_extract_{time}",
    format="{time} | {level} | {message} | {file}",
    colorize=True,
)


@extract_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=Dict[str, Sequence[Dict[str, Any]]],
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorMessageCommentariesNotFound}},
)
def find_all_commentaries():
    try:
        use_case = FindAllCommentariesUseCase(repository)
        found_comments: Optional[Sequence[OutputFindCommentaryDTO]] = use_case.execute()
        response = CommentaryPresenter().to_json(found_comments)
        return {"data": jsonable_encoder(response)}
    except CommentariesNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=exc.message
        ) from exc
    except Exception as exc:
        logger.error("Commentaries could not be found.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        ) from exc


@extract_router.get(
    "/id/{comment_id}/",
    status_code=status.HTTP_200_OK,
    response_model=Dict[str, List[Dict[str, Any]]],
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorMessageCommentaryNotFound}},
)
def find_commentary_by_id(comment_id: str):
    try:
        use_case = FindCommentaryByIDUseCase(repository)
        data = InputFindCommentaryByIDDTO(id=comment_id)
        found_commentary: Optional[OutputFindCommentaryDTO] = use_case.execute(data)
        response = CommentaryPresenter().to_json(found_commentary)
        return {"data": jsonable_encoder(response)}
    except CommentaryNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=exc.message
        ) from exc
    except Exception as exc:
        logger.error("Commentary could not be found by ID.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        ) from exc


@extract_router.get(
    "/instance/{comment_instance}/",
    status_code=status.HTTP_200_OK,
    response_model=Dict[str, List[Dict[str, Any]]],
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorMessageCommentaryNotFound}},
)
def find_commentary_by_email(comment_instance: str):
    try:
        use_case = FindCommentariesByInstanceSlugUseCase(repository)
        data = InputFindCommentaryByInstanceSlugDTO(instance_slug=comment_instance)
        found_comments: Optional[Sequence[OutputFindCommentaryDTO]] = use_case.execute(
            data
        )
        response = CommentaryPresenter().to_json(found_comments)
        return {"data": jsonable_encoder(response)}
    except CommentaryNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=exc.message
        ) from exc
    except Exception as exc:
        logger.error("Commentaries could not be found by instance slug.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        ) from exc


@extract_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=Dict[str, List[Dict[str, Any]]],
)
def add_new_commentary(new_comment: InputAddCommentaryDTO):
    try:
        use_case = AddCommentaryUseCase(repository)
        added_comment: OutputAddCommentaryDTO = use_case.execute(new_comment)
        response = CommentaryPresenter().to_json(added_comment)
        return {"data": jsonable_encoder(response)}
    except Exception as exc:
        logger.error("Commentary could not be added.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        ) from exc


@extract_router.delete(
    "/{comment_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None,
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorMessageCommentaryNotFound}},
)
def delete_commentary_by_id(comment_id: str):
    try:
        use_case = DeleteCommentaryUseCase(repository)
        data = InputDeleteCommentaryDTO(id=comment_id)
        use_case.execute(data)
    except CommentaryNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=exc.message
        ) from exc
    except Exception as exc:
        logger.error("Commentary could not be deleted.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        ) from exc
