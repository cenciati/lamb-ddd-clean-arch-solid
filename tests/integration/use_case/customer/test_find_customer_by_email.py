# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa


from pydantic import EmailStr

from src.application.use_case.customer.find.find_customer_by_email import (
    FindCustomerByEmailUseCase,
)
from src.application.use_case.customer.find.find_customer_dto import (
    InputFindCustomerDTO,
    OutputFindCustomerDTO,
)
from src.infrastructure.repository.memory.customer_memory_repository import (
    CustomerInMemoryRepository,
)


def test_find_customer_by_email_use_case_using_in_memory_repository(
    repository_with_customer_in_memory: CustomerInMemoryRepository,
) -> None:
    # Arrange
    use_case = FindCustomerByEmailUseCase(repository_with_customer_in_memory)
    email: EmailStr = list(repository_with_customer_in_memory.database.values())[
        0
    ].email
    customer = InputFindCustomerDTO(email=email)

    # Act
    found_customer: OutputFindCustomerDTO = use_case.execute(customer)

    # Assert
    assert found_customer.full_name == "John Doe"
    assert found_customer.email == email
    assert found_customer.cpf.number == "01234567890"
