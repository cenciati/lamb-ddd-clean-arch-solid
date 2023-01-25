from typing import Any, Dict, List, Optional, Sequence

from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from pydantic import EmailStr

from src.application.use_case.customer.add.add_customer import AddCustomerUseCase
from src.application.use_case.customer.add.add_customer_dto import InputAddCustomerDTO
from src.application.use_case.customer.delete.delete_customer import (
    DeleteCustomerUseCase,
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
from src.application.use_case.user.delete.delete_user_dto import InputDeleteUserDTO
from src.infrastructure.presentation.customer_presenter import CustomerPresenter
from src.infrastructure.repository.memory.customer_memory_repository import (
    CustomerInMemoryRepository,
)

customer_router = APIRouter(prefix="/customers")
repository = CustomerInMemoryRepository()


@customer_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=Dict[str, Sequence[Dict[str, Any]]],
)
async def find_all_customers():
    use_case = FindAllCustomersUseCase(repository)
    found_customers: Optional[Sequence[OutputFindCustomerDTO]] = use_case.execute()
    if not found_customers:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Any customer could not be found.",
        )
    response = CustomerPresenter().to_json(found_customers)
    return {"data": jsonable_encoder(response)}


@customer_router.get(
    "/id/{customer_id}/",
    status_code=status.HTTP_200_OK,
    response_model=Dict[str, List[Dict[str, Any]]],
)
async def find_customer_by_id(customer_id: str):
    use_case = FindCustomerByIDUseCase(repository)
    data = InputFindCustomerByIDDTO(id=customer_id)
    found_customer: Optional[OutputFindCustomerDTO] = use_case.execute(data)
    if not found_customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer could not be found."
        )
    response = CustomerPresenter().to_json(found_customer)
    return {"data": jsonable_encoder(response)}


@customer_router.get(
    "/email/{customer_email}/",
    status_code=status.HTTP_200_OK,
    response_model=Dict[str, List[Dict[str, Any]]],
)
async def find_customer_by_email(customer_email: EmailStr):
    use_case = FindCustomerByEmailUseCase(repository)
    data = InputFindCustomerByEmailDTO(email=customer_email)
    found_customer: Optional[OutputFindCustomerDTO] = use_case.execute(data)
    if not found_customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer could not be found."
        )
    response = CustomerPresenter().to_json(found_customer)
    return {"data": jsonable_encoder(response)}


@customer_router.get(
    "/cpf/{customer_cpf}/",
    status_code=status.HTTP_200_OK,
    response_model=Dict[str, List[Dict[str, Any]]],
)
async def find_customer_by_cpf(customer_cpf: str):
    use_case = FindCustomerByCpfUseCase(repository)
    data = InputFindCustomerByCpfDTO(cpf=customer_cpf)
    found_customer: Optional[OutputFindCustomerDTO] = use_case.execute(data)
    if not found_customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer could not be found."
        )
    response = CustomerPresenter().to_json(found_customer)
    return {"data": jsonable_encoder(response)}


@customer_router.post("/", status_code=status.HTTP_201_CREATED, response_model=None)
async def add_new_customer(new_customer: InputAddCustomerDTO):
    use_case = AddCustomerUseCase(repository)
    use_case.execute(new_customer)


@customer_router.delete(
    "/{customer_id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None
)
async def delte_customer_by_id(customer_id: str):
    use_case = DeleteCustomerUseCase(repository)
    data = InputDeleteUserDTO(id=customer_id)
    use_case.execute(data)
