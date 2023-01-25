# pylint: disable=consider-using-f-string
from typing import Any, Dict

import pytest
from fastapi import status
from fastapi.testclient import TestClient
from httpx import Response

from src.application.use_case.customer.add.add_customer_dto import (
    InputAddCustomerDTO,
    OutputAddCustomerDTO,
)
from src.application.use_case.customer.find.find_customer_dto import (
    OutputFindCustomerDTO,
)
from src.infrastructure.settings import Settings

settings = Settings()
base_url: str = f"{settings.BASE_URL}/customers"


@pytest.mark.e2e
def test_root_should_return_status_code_equal_to_404_if_there_are_no_registred_customer(
    client: TestClient,
) -> None:
    # Act
    response: Response = client.get(base_url)

    # Assert
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.e2e
def test_root_should_return_status_code_equal_to_200_if_there_are_registred_customers(
    client: TestClient,
) -> None:
    # Arrange
    new_customer = InputAddCustomerDTO(
        full_name="John Doe", email="johndoe@mail.com", cpf="01234567890"
    ).dict()
    added_customer: OutputAddCustomerDTO = client.post(
        base_url, json=new_customer
    ).json()["data"][0]

    # Act
    response: Response = client.get(base_url)

    # Teardown
    client.delete("{}/{}/".format(base_url, added_customer.get("id")))

    # Assert
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.e2e
def test_root_should_return_all_created_users(
    client: TestClient,
) -> None:
    # Arrange
    customer_1: Dict[str, Any] = InputAddCustomerDTO(
        full_name="John Doe", email="johndoe@mail.com", cpf="01234567890"
    ).dict()
    customer_2: Dict[str, Any] = InputAddCustomerDTO(
        full_name="Jane Doe", email="janendoe@mail.com", cpf="01234567891"
    ).dict()
    customer_3: Dict[str, Any] = InputAddCustomerDTO(
        full_name="Mark Doe", email="markndoe@mail.com", cpf="01234567892"
    ).dict()

    # Act
    added_customer_1: OutputAddCustomerDTO = client.post(
        base_url, json=customer_1
    ).json()["data"][0]
    added_customer_2: OutputAddCustomerDTO = client.post(
        base_url, json=customer_2
    ).json()["data"][0]
    added_customer_3: OutputAddCustomerDTO = client.post(
        base_url, json=customer_3
    ).json()["data"][0]

    # Teardown
    client.delete("{}/{}/".format(base_url, added_customer_1["id"]))
    client.delete("{}/{}/".format(base_url, added_customer_2["id"]))
    client.delete("{}/{}/".format(base_url, added_customer_3["id"]))

    # Assert
    assert added_customer_1["full_name"] == customer_1["full_name"]
    assert added_customer_1["email"] == customer_1["email"]
    assert added_customer_1["cpf"]["number"] == customer_1["cpf"]

    assert added_customer_2["full_name"] == customer_2["full_name"]
    assert added_customer_2["email"] == customer_2["email"]
    assert added_customer_2["cpf"]["number"] == customer_2["cpf"]

    assert added_customer_3["full_name"] == customer_3["full_name"]
    assert added_customer_3["email"] == customer_3["email"]
    assert added_customer_3["cpf"]["number"] == customer_3["cpf"]


@pytest.mark.e2e
def test_get_user_by_id_should_return_created_user(
    client: TestClient,
) -> None:
    # Arrange
    customer: Dict[str, Any] = InputAddCustomerDTO(
        full_name="John Doe", email="johndoe@mail.com", cpf="01234567890"
    ).dict()
    added_customer: OutputAddCustomerDTO = client.post(base_url, json=customer).json()[
        "data"
    ][0]

    # Act
    response: Response = client.get("{}/id/{}".format(base_url, added_customer["id"]))
    found_customer: OutputFindCustomerDTO = response.json()["data"][0]

    # Teardown
    client.delete("{}/{}/".format(base_url, added_customer["id"]))

    # Assert
    assert found_customer["full_name"] == customer["full_name"]
    assert found_customer["email"] == customer["email"]
    assert found_customer["cpf"]["number"] == customer["cpf"]


@pytest.mark.e2e
def test_get_user_by_email_should_return_created_user(
    client: TestClient,
) -> None:
    # Arrange
    customer: Dict[str, Any] = InputAddCustomerDTO(
        full_name="John Doe", email="johndoe@mail.com", cpf="01234567890"
    ).dict()
    added_customer: OutputAddCustomerDTO = client.post(base_url, json=customer).json()[
        "data"
    ][0]

    # Act
    response: Response = client.get(
        "{}/email/{}".format(base_url, added_customer["email"])
    )
    found_customer: OutputFindCustomerDTO = response.json()["data"][0]

    # Teardown
    client.delete("{}/{}/".format(base_url, added_customer["id"]))

    # Assert
    assert found_customer["full_name"] == customer["full_name"]
    assert found_customer["email"] == customer["email"]
    assert found_customer["cpf"]["number"] == customer["cpf"]


@pytest.mark.e2e
def test_get_user_by_cpf_should_return_created_user(
    client: TestClient,
) -> None:
    # Arrange
    customer: Dict[str, Any] = InputAddCustomerDTO(
        full_name="John Doe", email="johndoe@mail.com", cpf="01234567890"
    ).dict()
    added_customer: OutputAddCustomerDTO = client.post(base_url, json=customer).json()[
        "data"
    ][0]

    # Act
    response: Response = client.get(
        "{}/cpf/{}".format(base_url, added_customer["cpf"]["number"])
    )
    found_customer: OutputFindCustomerDTO = response.json()["data"][0]

    # Teardown
    client.delete("{}/{}/".format(base_url, added_customer["id"]))

    # Assert
    assert found_customer["full_name"] == customer["full_name"]
    assert found_customer["email"] == customer["email"]
    assert found_customer["cpf"]["number"] == customer["cpf"]


@pytest.mark.e2e
def test_delete_user_by_id_should_return_status_code_equal_to_204(
    client: TestClient,
) -> None:
    # Arrange
    customer: Dict[str, Any] = InputAddCustomerDTO(
        full_name="John Doe", email="johndoe@mail.com", cpf="01234567890"
    ).dict()
    added_customer: OutputAddCustomerDTO = client.post(base_url, json=customer).json()[
        "data"
    ][0]

    # Act
    response: Response = client.delete("{}/{}/".format(base_url, added_customer["id"]))

    # Assert
    assert response.status_code == status.HTTP_204_NO_CONTENT
