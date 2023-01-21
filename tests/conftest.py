import pytest

from src.application.use_case.user.dto.add_user_dto import AddUserDTO
from src.domain.entity.commentary import Commentary
from src.domain.value.rating import Rating
from src.domain.value.slug import Slug
from src.domain.value.tag import Tag
from src.infrastructure.repository.memory.user_memory_repository import (
    UserInMemoryRepository,
)


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


@pytest.fixture
def repository_with_user_in_memory() -> UserInMemoryRepository:
    new_user = AddUserDTO(
        email="johndoe@mail.com",
        password="iLoveApples2001",
        instance_slug=Slug(name="lamb"),
    )
    repository = UserInMemoryRepository()
    repository.add(new_user)
    return repository


@pytest.fixture
def repository_with_users_in_memory() -> UserInMemoryRepository:
    new_user_1 = AddUserDTO(
        email="larrygaham@mail.com",
        password="Dunno3222",
        instance_slug=Slug(name="lamb-1"),
    )
    new_user_2 = AddUserDTO(
        email="vanessamiwb@mail.com",
        password="wEIrDpass003woRd",
        instance_slug=Slug(name="lamb-2"),
    )
    new_user_3 = AddUserDTO(
        email="michaelrmanson@mail.com",
        password="allRIGHT2000Pass",
        instance_slug=Slug(name="lamb-3"),
    )
    repository = UserInMemoryRepository()
    repository.add(new_user_1)
    repository.add(new_user_2)
    repository.add(new_user_3)
    return repository
