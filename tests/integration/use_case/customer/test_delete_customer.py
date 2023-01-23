# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa
from pydantic import UUID4

from src.application.use_case.customer.delete.delete_customer import (
    DeleteCustomerUseCase,
)
from src.application.use_case.customer.delete.delete_customer_dto import (
    InputDeleteCustomerDTO,
)
from src.infrastructure.repository.memory.customer_memory_repository import (
    CustomerInMemoryRepository,
)


def test_delete_customer_use_case_using_in_memory_repository(
    repository_with_customer_in_memory: CustomerInMemoryRepository,
) -> None:
    # Arrange
    use_case = DeleteCustomerUseCase(repository_with_customer_in_memory)
    customer_id: UUID4 = list(repository_with_customer_in_memory.database.keys())[0]
    deleted_customer = InputDeleteCustomerDTO(id=customer_id)

    # Act
    use_case.execute(deleted_customer)
    database_length: int = len(repository_with_customer_in_memory.database)

    # Assert
    assert database_length == 0
