from pathlib import Path

import pytest
import testing.postgresql
from flask import Flask
from sqlalchemy import create_engine, Connection, Engine, text

from webapp import app
from webapp.config import AppConfig

ROOT_DIR = (Path(__file__).parents[1]).resolve()


def setup_db(db_uri: str) -> None:
    """
    Creates and populates the tables for the given URI.
    The URI should be the administative user (`postgres`) so that we can
    correctly execute our setup.
    """
    ddl_dir = ROOT_DIR / "ddl"
    engine = create_engine(db_uri)
    with engine.connect() as conn:
        with conn.begin():
            for path in sorted(ddl_dir.glob("*.sql")):
                with path.open() as file_:
                    sql = file_.read()
                conn.execute(text(sql))
                print(f"Running {path}")


@pytest.fixture(scope="module")
def db() -> Engine:
    """
    Create a dummy database that can be used by our application.

    Because of the time that it takes to instantiate the database with the correct
    shape, we will only do the creation once for each module.
    """
    with testing.postgresql.Postgresql() as pg:
        admin_db_uri = pg.url(user="postgres:postgres")
        setup_db(admin_db_uri)

        db_uri = pg.url(user="example_user:example")
        engine = create_engine(db_uri)
        yield engine


@pytest.fixture()
def webapp(db) -> Flask:
    """Returns a running flask application in testing mode"""
    config = AppConfig(
        DB_URI=db.url.render_as_string(hide_password=False),
        PORT="8001"
    )
    client = app.create_app(config).test_client()
    yield client
