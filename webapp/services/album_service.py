from sqlalchemy.engine import Connection

from webapp.models.album import Album
from webapp.daos import album_dao, artist_dao


def create(conn: Connection, album: Album) -> None:
    with conn.begin():
        # if we don't have an artist for that name, just create it
        artist = artist_dao.get_artist_from_name(conn, album.artist_name)
        if artist is None:
            artist = artist_dao.create_artist_from_name(conn, album.artist_name)
        album_dao.create_album(conn, album, artist_id=artist.id)
