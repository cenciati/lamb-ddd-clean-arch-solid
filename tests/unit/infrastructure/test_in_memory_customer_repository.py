# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa


from sqlalchemy import Sequence

from src.application.use_case.customer.add.add_customer_dto import InputAddCustomerDTO
from src.application.use_case.customer.find.find_customer_dto import (
    InputFindCustomerByCpfDTO,
    InputFindCustomerByEmailDTO,
    InputFindCustomerByIDDTO,
    OutputFindCustomerDTO,
)
from src.application.use_case.user.delete.delete_user_dto import InputDeleteUserDTO
from src.infrastructure.repository.memory.customer_memory_repository import (
    CustomerInMemoryRepository,
)


def test_add_new_customer_in_memory() -> None:
    # Arrange
    new_customer = InputAddCustomerDTO(
        full_name="John Doe", email="johndoe@mail.com", cpf="01234567890"
    )

    # Act
    customer_repository = CustomerInMemoryRepository()
    customer_repository.add(new_customer)
    database: list = list(customer_repository.database.values())

    # Assert
    assert len(customer_repository.database) == 1
    assert database[0].full_name == "John Doe"
    assert database[0].email == "johndoe@mail.com"
    assert database[0].cpf.number == "01234567890"


def test_find_customer_in_memory(
    repository_with_customer_in_memory: CustomerInMemoryRepository,
) -> None:
    # Arrange
    created_customer_id: str = str(
        list(repository_with_customer_in_memory.database.keys())[0]
    )
    customer = InputFindCustomerByIDDTO(id=created_customer_id)

    # Act
    found_customer: OutputFindCustomerDTO = repository_with_customer_in_memory.find(
        customer
    )

    # Assert
    assert len(repository_with_customer_in_memory.database) == 1
    assert found_customer.full_name == "John Doe"
    assert found_customer.email == "johndoe@mail.com"
    assert found_customer.cpf.number == "01234567890"


def test_find_customer_by_email_in_memory(
    repository_with_customer_in_memory: CustomerInMemoryRepository,
) -> None:
    # Arrange
    customer = InputFindCustomerByEmailDTO(email="johndoe@mail.com")

    # Act
    found_customer: OutputFindCustomerDTO = (
        repository_with_customer_in_memory.find_by_email(customer)
    )

    # Assert
    assert len(repository_with_customer_in_memory.database) == 1
    assert found_customer.full_name == "John Doe"
    assert found_customer.email == "johndoe@mail.com"
    assert found_customer.cpf.number == "01234567890"


def test_find_customer_by_cpf_in_memory(
    repository_with_customer_in_memory: CustomerInMemoryRepository,
) -> None:
    # Arrange
    customer = InputFindCustomerByCpfDTO(cpf="01234567890")

    # Act
    found_customer: OutputFindCustomerDTO = (
        repository_with_customer_in_memory.find_by_cpf(customer)
    )

    # Assert
    assert len(repository_with_customer_in_memory.database) == 1
    assert found_customer.full_name == "John Doe"
    assert found_customer.email == "johndoe@mail.com"
    assert found_customer.cpf.number == "01234567890"


def test_find_all_customers_in_memory(
    repository_with_customers_in_memory: CustomerInMemoryRepository,
) -> None:
    # Arrange

    # Act
    all_customers: Sequence[
        OutputFindCustomerDTO
    ] = repository_with_customers_in_memory.find_all()
    customers_amount_length: int = len(repository_with_customers_in_memory.database)

    # Assert
    assert customers_amount_length == 3

    assert all_customers[0].full_name == "John Doe"
    assert all_customers[0].email == "johndoe@mail.com"
    assert all_customers[0].cpf.number == "01234567890"

    assert all_customers[1].full_name == "Mark Blo"
    assert all_customers[1].email == "markblo@mail.com"
    assert all_customers[1].cpf.number == "01234567891"

    assert all_customers[2].full_name == "Vanessa Suhm"
    assert all_customers[2].email == "vanessasuhm@mail.com"
    assert all_customers[2].cpf.number == "01234567892"


def test_delete_customer_in_memory(
    repository_with_customer_in_memory: CustomerInMemoryRepository,
) -> None:
    # Act
    customer_id: str = str(list(repository_with_customer_in_memory.database.keys())[0])
    deleted_customer = InputDeleteUserDTO(id=customer_id)
    repository_with_customer_in_memory.delete(deleted_customer)

    # Assert
    assert len(repository_with_customer_in_memory.database) == 0
