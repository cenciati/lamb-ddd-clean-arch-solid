# import pytest
# from fastapi import status
# from fastapi.testclient import TestClient
# from httpx import Response

# from src.infrastructure.settings import Settings

# settings = Settings()
# base_url: str = f"{settings.BASE_URL}/customers"


# @pytest.mark.e2e
# def test_get_request_to_find_a_customer_by_id_should_return_status_code_equal_to_200(
#     client: TestClient,
# ) -> None:
#     # Act
#     response: Response = client.get(base_url)

#     # Assert
#     assert response.status_code == status.HTTP_200_OK


# @pytest.mark.e2e
# def test_make_a_get_request_body_should_return_list_of_data(
#     client: TestClient,
# ) -> None:
#     # Act
#     response: Response = client.get(base_url)

#     # Assert
#     assert isinstance(response.json()["data"], list)
#     assert response.json()["data"] == [{"Go to:": "/extract"}]
