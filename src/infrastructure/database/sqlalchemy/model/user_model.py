# pylint: disable=no-name-in-module
from sqlalchemy import Column, DateTime, String
from sqlalchemy.sql import func

from src.infrastructure.database.sqlalchemy.db_base import Base


class UserModel(Base):
    """SQLAlchemy user table mapping."""

    __tablename__ = "users"
    id = Column(String, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String(32), nullable=False)
    instance_slug = Column(String(24), nullable=False)
    created_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    def __repr__(self) -> str:
        return f"""<UserModel(id={self.id},
        email={self.email},
        password={self.password},
        instance_slug={self.instance_slug},
        created_at={self.created_at},
        updated_at={self.updated_at})>"""

    def __eq__(self, other: object) -> bool:
        return (
            self.id == other.id
            and self.email == other.email
            and self.password == other.password
            and self.instance_slug == other.instance_slug
            and self.created_at == other.created_at
            and self.updated_at == other.updated_at
        )
