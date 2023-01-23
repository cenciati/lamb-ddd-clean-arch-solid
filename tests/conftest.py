# pylint: disable=redefined-outer-name
from uuid import uuid4

import pytest

from src.application.use_case.commentary.add.add_commentary_dto import (
    InputAddCommentaryDTO,
)
from src.application.use_case.customer.add.add_customer_dto import InputAddCustomerDTO
from src.application.use_case.user.add.add_user_dto import InputAddUserDTO
from src.domain.entity.commentary import Commentary
from src.domain.value.cpf import Cpf
from src.domain.value.rating import Rating
from src.domain.value.slug import Slug
from src.domain.value.tag import Tag
from src.infrastructure.repository.memory.commentary_memory_repository import (
    CommentaryInMemoryRepository,
)
from src.infrastructure.repository.memory.customer_memory_repository import (
    CustomerInMemoryRepository,
)
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
def new_comment() -> InputAddCommentaryDTO:
    return InputAddCommentaryDTO(
        content="The experience was great in general.",
        rating=Rating(score=9),
        tags=[
            Tag(id=0, name="Experience", sentiment=1, subtag=False),
            Tag(id=1, name="Infrastructure", sentiment=1, subtag=False),
        ],
        customer_id=uuid4(),
        instance_slug=Slug(name="lamb"),
        journey_slug=Slug(name="site"),
    )


@pytest.fixture
def repository_with_comment_in_memory(
    new_comment: InputAddCommentaryDTO,
) -> CommentaryInMemoryRepository:
    repository = CommentaryInMemoryRepository()
    repository.add(new_comment)
    return repository


@pytest.fixture
def repository_with_comments_in_memory() -> CommentaryInMemoryRepository:
    new_comment_1 = InputAddCommentaryDTO(
        content="The experience was great in general.",
        rating=Rating(score=9),
        tags=[
            Tag(id=0, name="Experience", sentiment=1, subtag=False),
            Tag(id=1, name="Infrastructure", sentiment=1, subtag=False),
        ],
        customer_id=uuid4(),
        instance_slug=Slug(name="lamb"),
        journey_slug=Slug(name="site"),
    )
    new_comment_2 = InputAddCommentaryDTO(
        content="It doesn't work properly.",
        rating=Rating(score=2),
        tags=[
            Tag(id=0, name="Experience", sentiment=0, subtag=False),
        ],
        customer_id=uuid4(),
        instance_slug=Slug(name="lamb"),
        journey_slug=Slug(name="app"),
    )
    new_comment_3 = InputAddCommentaryDTO(
        content="Support took a while to reply.",
        rating=Rating(score=5),
        tags=[
            Tag(id=0, name="Experience", sentiment=1, subtag=False),
            Tag(id=2, name="Support", sentiment=0, subtag=False),
            Tag(id=3, name="Support - Agility", sentiment=0, subtag=True),
        ],
        customer_id=uuid4(),
        instance_slug=Slug(name="lamb"),
        journey_slug=Slug(name="site"),
    )
    repository = CommentaryInMemoryRepository()
    repository.add(new_comment_1)
    repository.add(new_comment_2)
    repository.add(new_comment_3)
    return repository


@pytest.fixture
def repository_with_user_in_memory() -> UserInMemoryRepository:
    new_user = InputAddUserDTO(
        email="johndoe@mail.com",
        password="iLoveApples2001",
        instance_slug=Slug(name="lamb"),
    )
    repository = UserInMemoryRepository()
    repository.add(new_user)
    return repository


@pytest.fixture
def repository_with_users_in_memory() -> UserInMemoryRepository:
    new_user_1 = InputAddUserDTO(
        email="larrygaham@mail.com",
        password="Dunno3222",
        instance_slug=Slug(name="lamb-1"),
    )
    new_user_2 = InputAddUserDTO(
        email="vanessamiwb@mail.com",
        password="wEIrDpass003woRd",
        instance_slug=Slug(name="lamb-2"),
    )
    new_user_3 = InputAddUserDTO(
        email="michaelrmanson@mail.com",
        password="allRIGHT2000Pass",
        instance_slug=Slug(name="lamb-3"),
    )
    repository = UserInMemoryRepository()
    repository.add(new_user_1)
    repository.add(new_user_2)
    repository.add(new_user_3)
    return repository


@pytest.fixture
def repository_with_customer_in_memory() -> CustomerInMemoryRepository:
    new_customer = InputAddCustomerDTO(
        full_name="John Doe",
        email="johndoe@mail.com",
        cpf=Cpf(number="01234567890"),
    )
    repository = CustomerInMemoryRepository()
    repository.add(new_customer)
    return repository


@pytest.fixture
def repository_with_customers_in_memory() -> CustomerInMemoryRepository:
    new_customer_1 = InputAddCustomerDTO(
        full_name="John Doe",
        email="johndoe@mail.com",
        cpf=Cpf(number="01234567890"),
    )
    new_customer_2 = InputAddCustomerDTO(
        full_name="Mark Blo",
        email="markblo@mail.com",
        cpf=Cpf(number="01234567891"),
    )
    new_customer_3 = InputAddCustomerDTO(
        full_name="Vanessa Suhm",
        email="vanessasuhm@mail.com",
        cpf=Cpf(number="01234567892"),
    )
    repository = CustomerInMemoryRepository()
    repository.add(new_customer_1)
    repository.add(new_customer_2)
    repository.add(new_customer_3)
    return repository
