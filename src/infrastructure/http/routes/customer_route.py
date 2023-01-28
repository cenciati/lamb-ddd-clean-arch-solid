from typing import Any, Dict, List, Optional, Sequence

from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from loguru import logger
from pydantic import EmailStr

from src.application.use_case.customer.add.add_customer import AddCustomerUseCase
from src.application.use_case.customer.add.add_customer_dto import (
    InputAddCustomerDTO,
    OutputAddCustomerDTO,
)
from src.application.use_case.customer.delete.delete_customer import (
    DeleteCustomerUseCase,
)
from src.application.use_case.customer.delete.delete_customer_dto import (
    InputDeleteCustomerDTO,
)
from src.application.use_case.customer.find.find_all_customers import (
    FindAllCustomersUseCase,
)
from src.application.use_case.customer.find.find_customer_by_cpf import (
    FindCustomerByCpfUseCase,
)
from src.application.use_case.customer.find.find_customer_by_email import (
    FindCustomerByEmailUseCase,
)
from src.application.use_case.customer.find.find_customer_by_id import (
    FindCustomerByIDUseCase,
)
from src.application.use_case.customer.find.find_customer_dto import (
    InputFindCustomerByCpfDTO,
    InputFindCustomerByEmailDTO,
    InputFindCustomerByIDDTO,
    OutputFindCustomerDTO,
)
from src.domain.error.customer_exception import (
    CustomerDuplicateEmailError,
    CustomerNotFoundError,
    CustomersNotFoundError,
)
from src.infrastructure.presentation.data.customer_presenter import CustomerPresenter
from src.infrastructure.presentation.error.customer_exception_presentation import (
    ErrorMessageCustomerDuplicateEmail,
    ErrorMessageCustomerNotFound,
    ErrorMessageCustomersNotFound,
)
from src.infrastructure.repository.memory.customer_memory_repository import (
    CustomerInMemoryRepository,
)

customer_router = APIRouter(prefix="/customers")
repository = CustomerInMemoryRepository()
logger.add(
    "./reports/logs/api_customers_{time}",
    format="{time} | {level} | {message} | {file}",
    colorize=True,
)


@customer_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=Dict[str, Sequence[Dict[str, Any]]],
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorMessageCustomersNotFound}},
)
def find_all_customers():
    try:
        use_case = FindAllCustomersUseCase(repository)
        found_customers: Optional[Sequence[OutputFindCustomerDTO]] = use_case.execute()
        response = CustomerPresenter().to_json(found_customers)
        return {"data": jsonable_encoder(response)}
    except CustomersNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=exc.message
        ) from exc
    except Exception as exc:
        logger.error("Customers could not be found.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        ) from exc


@customer_router.get(
    "/id/{customer_id}/",
    status_code=status.HTTP_200_OK,
    response_model=Dict[str, List[Dict[str, Any]]],
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorMessageCustomerNotFound}},
)
def find_customer_by_id(customer_id: str):
    try:
        use_case = FindCustomerByIDUseCase(repository)
        data = InputFindCustomerByIDDTO(id=customer_id)
        found_customer: Optional[OutputFindCustomerDTO] = use_case.execute(data)
        response = CustomerPresenter().to_json(found_customer)
        return {"data": jsonable_encoder(response)}
    except CustomerNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=exc.message
        ) from exc
    except Exception as exc:
        logger.error("Customer could not be found by ID.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        ) from exc


@customer_router.get(
    "/email/{customer_email}/",
    status_code=status.HTTP_200_OK,
    response_model=Dict[str, List[Dict[str, Any]]],
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorMessageCustomerNotFound}},
)
def find_customer_by_email(customer_email: EmailStr):
    try:
        use_case = FindCustomerByEmailUseCase(repository)
        data = InputFindCustomerByEmailDTO(email=customer_email)
        found_customer: Optional[OutputFindCustomerDTO] = use_case.execute(data)
        response = CustomerPresenter().to_json(found_customer)
        return {"data": jsonable_encoder(response)}
    except CustomerNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=exc.message
        ) from exc
    except Exception as exc:
        logger.error("Customer could not be found by e-mail.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        ) from exc


@customer_router.get(
    "/cpf/{customer_cpf}/",
    status_code=status.HTTP_200_OK,
    response_model=Dict[str, List[Dict[str, Any]]],
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorMessageCustomerNotFound}},
)
def find_customer_by_cpf(customer_cpf: str):
    try:
        use_case = FindCustomerByCpfUseCase(repository)
        data = InputFindCustomerByCpfDTO(cpf=customer_cpf)
        found_customer: Optional[OutputFindCustomerDTO] = use_case.execute(data)
        response = CustomerPresenter().to_json(found_customer)
        return {"data": jsonable_encoder(response)}
    except CustomerNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=exc.message
        ) from exc
    except Exception as exc:
        logger.error("Customer could not be found by CPF.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        ) from exc


@customer_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=Dict[str, List[Dict[str, Any]]],
    responses={
        status.HTTP_409_CONFLICT: {
            "model": ErrorMessageCustomerDuplicateEmail,
        }
    },
)
def add_new_customer(new_customer: InputAddCustomerDTO):
    try:
        use_case = AddCustomerUseCase(repository)
        added_customer: OutputAddCustomerDTO = use_case.execute(new_customer)
        response = CustomerPresenter().to_json(added_customer)
        return {"data": jsonable_encoder(response)}
    except CustomerDuplicateEmailError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=exc.message
        ) from exc
    except Exception as exc:
        logger.error("Customer could not be added.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        ) from exc


@customer_router.delete(
    "/{customer_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None,
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorMessageCustomerNotFound}},
)
def delete_customer_by_id(customer_id: str):
    try:
        use_case = DeleteCustomerUseCase(repository)
        data = InputDeleteCustomerDTO(id=customer_id)
        use_case.execute(data)
    except CustomerNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=exc.message
        ) from exc
    except Exception as exc:
        logger.error("Customer could not be deleted.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        ) from exc
