from typing import Optional

from sqlalchemy import text
from sqlalchemy.engine import Connection
from sqlalchemy.exc import NoResultFound

from webapp.models.album import Album


def get_album(conn: Connection, album_id: str) -> Optional[Album]:
    sql = """
    select album.id, album.title, artist.name as artist_name
    from example.album
    join example.artist on album.artist_id = artist.id
    where album.id = :id
    """
    params = {"id": album_id}
    try:
        result = conn.execute(text(sql), params).mappings().one()
    except NoResultFound:
        return None
    return Album(**result)


def create_album(conn: Connection, album: Album, *, artist_id: str) -> Album:
    sql = """
    insert into example.album (id, artist_id, title)
    values (:id, :artist_id, :title)
    """
    params = {**album.model_dump(), "artist_id": artist_id}
    conn.execute(text(sql), params)
    album = get_album(conn, album.id)
    if album is None:
        raise ValueError(
            f"Unable to successfully create album for {album.model_dump()}"
        )
    return album
