from webapp.database import engine
from webapp.models.album import Album
from webapp.services import album_service


def create(album: Album) -> None:
    with engine.connect() as conn:
        album_service.create(conn, album)
