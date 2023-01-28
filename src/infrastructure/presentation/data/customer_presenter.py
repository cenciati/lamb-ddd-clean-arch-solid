from typing import Any, Dict, List, Sequence

from src.application.use_case.customer.add.add_customer_dto import OutputAddCustomerDTO
from src.application.use_case.customer.find.find_customer_dto import (
    OutputFindCustomerDTO,
)


class CustomerPresenter:
    """Presentation layer for customer entities."""

    @classmethod
    def to_json(
        cls,
        data: OutputAddCustomerDTO
        | OutputFindCustomerDTO
        | Sequence[OutputAddCustomerDTO]
        | Sequence[OutputFindCustomerDTO],
    ) -> List[Dict[str, Any]]:
        """Transform a data transfer object into a
            presentable json response for HTTP.
        Args:
            data (OutputFindCustomerDTO): Input data to be
                converted to JSON format.
        Returns:
            Presentable dictionary for HTTP responses.
        """
        if isinstance(data, list):
            return [customer.dict() for customer in data]
        return [data.dict()]
