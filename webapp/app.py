import os

from flask import Flask
from pydantic import BaseModel

from webapp.api import health


blueprints = [
    health.blueprint
]


class AppConfig(BaseModel):
    """Defines the necessary configuration for the Flask application to run"""

    DEBUG: bool = True
    HOST: str = "0.0.0.0"
    PORT: str = "8000"
    SECRET_KEY: str = "dev"

    @classmethod
    def from_env(cls) -> "AppConfig":
        """
        Returns an AppConfig instance sourced from what the values stored in
        `os.environ`.

        This should be capable of automatically detecting any variable whose
        name exactly matches the class's attribute name.
        """
        return AppConfig(**os.environ)


def create_app(config: AppConfig) -> Flask:
    """
    Creates a Flask application instance with the defined configuration and
    all targeted blueprints registered
    """
    app = Flask(__name__)
    app.config.from_mapping(**config.model_dump())

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    return app
