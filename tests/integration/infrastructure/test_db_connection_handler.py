# pylint: disable=line-too-long, protected-access, no-name-in-module, broad-except
# flake8: noqa

import pytest
from sqlalchemy.engine.base import Engine

from src.infrastructure.database.sqlalchemy.db_connection_handler import (
    DBConnectionHandler,
)


@pytest.mark.need_dot_env
def test_get_engine_should_return_sql_alchemy_new_engine_object() -> None:
    # Arrange
    db_connection_handler = DBConnectionHandler()

    # Act
    new_engine: Engine = db_connection_handler.get_engine()

    # Assert
    assert isinstance(new_engine, Engine)


@pytest.mark.need_dot_env
def test_when_enter_into_a_new_database_session_context_should_not_raise_an_error() -> None:
    with DBConnectionHandler() as db_connection_handler:
        try:
            db_connection_handler.session.close()
            assert True
        except Exception:
            assert False
