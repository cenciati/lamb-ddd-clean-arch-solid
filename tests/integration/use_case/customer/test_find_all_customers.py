# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa


from typing import Sequence

from src.application.use_case.customer.find.find_all_customers import (
    FindAllCustomersUseCase,
)
from src.application.use_case.customer.find.find_customer_dto import (
    OutputFindCustomerDTO,
)
from src.infrastructure.repository.memory.customer_memory_repository import (
    CustomerInMemoryRepository,
)


def test_find_all_customers_found_use_case_using_in_memory_repository(
    repository_with_customers_in_memory: CustomerInMemoryRepository,
) -> None:
    # Arrange
    use_case = FindAllCustomersUseCase(repository_with_customers_in_memory)

    # Act
    all_customers_found: Sequence[OutputFindCustomerDTO] = use_case.execute()
    customers_amount_length: int = len(all_customers_found)

    # Assert
    assert customers_amount_length == 3

    assert all_customers_found[0].full_name == "John Doe"
    assert all_customers_found[0].email == "johndoe@mail.com"
    assert all_customers_found[0].cpf.number == "01234567890"

    assert all_customers_found[1].full_name == "Mark Blo"
    assert all_customers_found[1].email == "markblo@mail.com"
    assert all_customers_found[1].cpf.number == "94658372029"

    assert all_customers_found[2].full_name == "Vanessa Suhm"
    assert all_customers_found[2].email == "vanessasuhm@mail.com"
    assert all_customers_found[2].cpf.number == "84184182062"
