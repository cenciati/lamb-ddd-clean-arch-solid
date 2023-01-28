# pylint: disable=no-name-in-module
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String

from src.infrastructure.database.sqlalchemy.db_base import Base


class CommentaryModel(Base):
    """SQLAlchemy commentary table mapping."""

    __tablename__ = "commentaries"
    id = Column(String, primary_key=True)
    content = Column(String(2000), nullable=False)
    rating = Column(Integer, nullable=False)
    tags = Column(String, nullable=False)
    customer_id = Column(String, ForeignKey("customers.id"))
    instance_slug = Column(String(24), nullable=False)
    journey_slug = Column(String(24), nullable=False)
    automatic = Column(Boolean, nullable=False)
    experience_date = Column(DateTime(timezone=True), nullable=False)

    def __repr__(self) -> str:
        return f"""
            <CommentaryModel(id={self.id},
            content={self.content},
            rating={self.rating},
            tags={self.tags},
            customer_id={self.customer_id},
            instance_slug={self.instance_slug},
            journey_slug={self.journey_slug},
            automatic={self.automatic},
            experience_date={self.experience_date})>
            """

    def __eq__(self, other: object) -> bool:
        return (
            self.id == other.id
            and self.content == other.content
            and self.rating == other.rating
            and self.tags == other.tags
            and self.customer_id == other.customer_id
            and self.instance_slug == other.instance_slug
            and self.journey_slug == other.journey_slug
            and self.automatic == other.automatic
            and self.experience_date == other.experience_date
        )
