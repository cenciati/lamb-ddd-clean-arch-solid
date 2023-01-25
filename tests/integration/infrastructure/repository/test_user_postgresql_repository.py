# from faker import Faker
# from sqlalchemy.engine import Engine

# from src.application.use_case.user.add.add_user_dto import InputAddUserDTO
# from src.domain.value.slug import Slug
# from src.infrastructure.database.sqlalchemy.db_connection_handler import (
#     DBConnectionHandler,
# )
# from src.infrastructure.database.sqlalchemy.model.user_model import UserModel
# from src.infrastructure.repository.postgresql.user_postgresql_repository import (
#     UserPostgreSQLRepository,
# )


# def test_add_user() -> None:
#     # Arrange
#     faker = Faker()
#     email: str = faker.email()
#     password: str = faker.text(10)
#     slug: Slug = Slug(name="lamb")
#     db_handler = DBConnectionHandler()
#     engine: Engine = db_handler.get_engine()
#     repository = UserPostgreSQLRepository(db_handler)
#     new_user = InputAddUserDTO(
#         email=email,
#         password=password,
#         instance_slug=slug,
#     )

#     # Act
#     repository.add(new_user)
#     found_user: UserModel = engine.execute(
#         f"SELECT * FROM users WHERE email = '{email}'"
#     ).fetchone()

#     # Teardown
#     engine.execute(f"DELETE FROM users WHERE email = '{email}'")

#     # Assert
#     assert found_user is not None
#     assert found_user.email == email
#     assert found_user.password == password
#     assert found_user.instance_slug == slug
