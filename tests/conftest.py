import pytest

from src.domain.entity.commentary import Commentary
from src.domain.value.rating import Rating
from src.domain.value.slug import Slug
from src.domain.value.tag import Tag


@pytest.fixture
def comment() -> Commentary:
    return Commentary(
        content="Test comment.",
        rating=Rating(score=9),
        customer_id="ef29ffc3-9ef3-40f5-842d-8403c5eccde1",
        instance_slug=Slug(name="lamb"),
        journey_slug=Slug(name="generic"),
    )


@pytest.fixture
def comment_with_tags() -> Commentary:
    return Commentary(
        content="Test comment.",
        rating=Rating(score=9),
        tags=[
            Tag(id=1, name="Delivery", sentiment=1, subtag=False),
            Tag(id=2, name="Delivery - Time", sentiment=0, subtag=True),
            Tag(id=3, name="People", sentiment=1, subtag=False),
            Tag(id=4, name="Quality", sentiment=1, subtag=False),
        ],
        customer_id="ef29ffc3-9ef3-40f5-842d-8403c5eccde1",
        instance_slug=Slug(name="lamb"),
        journey_slug=Slug(name="generic"),
    )
