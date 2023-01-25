# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa


from pydantic import UUID4

from src.application.use_case.customer.find.find_customer_by_id import (
    FindCustomerByIDUseCase,
)
from src.application.use_case.customer.find.find_customer_dto import (
    InputFindCustomerByIDDTO,
    OutputFindCustomerDTO,
)
from src.infrastructure.repository.memory.customer_memory_repository import (
    CustomerInMemoryRepository,
)


def test_find_customer_by_id_use_case_using_in_memory_repository(
    repository_with_customer_in_memory: CustomerInMemoryRepository,
) -> None:
    # Arrange
    use_case = FindCustomerByIDUseCase(repository_with_customer_in_memory)
    customer_id: str = str(list(repository_with_customer_in_memory.database.keys())[0])
    customer = InputFindCustomerByIDDTO(id=customer_id)

    # Act
    found_customer: OutputFindCustomerDTO = use_case.execute(customer)

    # Assert
    assert found_customer.id == UUID4(customer_id)
    assert found_customer.full_name == "John Doe"
    assert found_customer.email == "johndoe@mail.com"
    assert found_customer.cpf.number == "01234567890"
