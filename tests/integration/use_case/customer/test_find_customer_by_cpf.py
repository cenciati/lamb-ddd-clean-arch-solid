# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa


from src.application.use_case.customer.find.find_customer_by_cpf import (
    FindCustomerByCpfUseCase,
)
from src.application.use_case.customer.find.find_customer_dto import (
    InputFindCustomerDTO,
    OutputFindCustomerDTO,
)
from src.domain.value.cpf import Cpf
from src.infrastructure.repository.memory.customer_memory_repository import (
    CustomerInMemoryRepository,
)


def test_find_customer_by_cpf_use_case_using_in_memory_repository(
    repository_with_customer_in_memory: CustomerInMemoryRepository,
) -> None:
    # Arrange
    use_case = FindCustomerByCpfUseCase(repository_with_customer_in_memory)
    cpf: Cpf = list(repository_with_customer_in_memory.database.values())[0].cpf
    customer = InputFindCustomerDTO(cpf=cpf)

    # Act
    found_customer: OutputFindCustomerDTO = use_case.execute(customer)

    # Assert
    assert found_customer.full_name == "John Doe"
    assert found_customer.email == "johndoe@mail.com"
    assert found_customer.cpf.number == cpf.number
