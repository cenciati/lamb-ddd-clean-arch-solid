# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa


from src.application.use_case.customer.add.add_customer import AddCustomerUseCase
from src.application.use_case.customer.add.add_customer_dto import InputAddCustomerDTO
from src.application.use_case.customer.find.find_customer_dto import (
    OutputFindCustomerDTO,
)
from src.infrastructure.repository.memory.customer_memory_repository import (
    CustomerInMemoryRepository,
)


def test_add_customer_use_case_using_in_memory_repository() -> None:
    # Arrange
    new_customer = InputAddCustomerDTO(
        full_name="John Doe", email="johndoe@mail.com", cpf="01234567890"
    )
    repository = CustomerInMemoryRepository()
    use_case = AddCustomerUseCase(repository)

    # Act
    use_case.execute(new_customer)
    added_customer: OutputFindCustomerDTO = list(repository.database.values())[0]

    # Assert
    assert added_customer.full_name == "John Doe"
    assert added_customer.email == "johndoe@mail.com"
    assert added_customer.cpf.number == "01234567890"
