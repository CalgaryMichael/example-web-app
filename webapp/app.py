from flask import Flask

from webapp.api import album, artist, health
from webapp.config import AppConfig
from webapp.database import engine


blueprints = [
    album.blueprint,
    artist.blueprint,
    health.blueprint,
]


def create_app(config: AppConfig) -> Flask:
    """
    Creates a Flask application instance with the defined configuration and
    all targeted blueprints registered
    """
    app = Flask(__name__)
    app.config.from_mapping(**config.model_dump())

    # initialize connection to the DB so that we know the application will
    # run properly
    engine.initialize(config)

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    return app
