from contextlib import contextmanager

from sqlalchemy import create_engine, Engine
from sqlalchemy.engine import Connection

from webapp.config import AppConfig


class EngineWrapper:
    """
    A wrapper around SQLAlchemy's Engine that allows us to hold
    the initialize the instance from AppConfig that are generated at runtime.
    Using this class as a singleton ensures that all routes that need to access
    the Engine instance can once we have started the application.
    """
    __engine: None

    def initialize(self, config: AppConfig) -> None:
        """
        This will create a connection to the DB specified in the configuration
        and check to ensure that the DB is live before returning.
        If the DB is not live, this will throw an error
        """
        self.__engine = create_engine(config.DB_URI, pool_pre_ping=True)

    def get_engine(self) -> Engine:
        if self.__engine is None:
            raise ValueError("Engine has not been initialized yet")
        return self.__engine

    @contextmanager
    def connect(self) -> Connection:
        e = self.get_engine()
        with e.connect() as conn:
            yield conn


engine = EngineWrapper()
