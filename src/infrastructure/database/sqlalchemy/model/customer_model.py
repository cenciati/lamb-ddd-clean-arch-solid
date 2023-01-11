# pylint: disable=no-name-in-module
from sqlalchemy import Column, String

from src.infrastructure.database.sqlalchemy.db_config import Base


class CustomerModel(Base):
    """SQLAlchemy customer table mapping."""

    __tablename__ = "customers"
    id = Column(String, primary_key=True)
    full_name = Column(String(64), nullable=False)
    email = Column(String, nullable=False, unique=True)
    cpf = Column(String(11), nullable=False, unique=True)

    def __repr__(self) -> str:
        return f"""
            <CustomerModel(id={self.id},
            full_name={self.full_name},
            email={self.email},
            cpf={self.cpf},
            """

    def __eq__(self, other) -> bool:
        return (
            self.id == other.id
            and self.full_name == other.full_name
            and self.email == other.name
            and self.cpf == other.cpf
        )
