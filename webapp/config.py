import os

from pydantic import BaseModel


class AppConfig(BaseModel):
    """Defines the necessary configuration for the Flask application to run"""

    DB_URI: str
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
