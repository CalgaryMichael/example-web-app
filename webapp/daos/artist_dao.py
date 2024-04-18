from typing import Optional

from sqlalchemy import text
from sqlalchemy.engine import Connection
from sqlalchemy.exc import NoResultFound

from webapp.models.artist import Artist


def get_all_artists(conn: Connection) -> list[Artist]:
    sql = """
    select id, name
    from example.artist
    group by 1, 2
    """
    return [
        Artist(**result)
        for result
        in conn.execute(text(sql)).mappings().all()
    ]


def get_artist_from_name(conn: Connection, name: str) -> Optional[Artist]:
    sql = """
    select id, name
    from example.artist
    where name = :name
    """
    params = {"name": name}
    try:
        result = conn.execute(text(sql), params).mappings().one()
    except NoResultFound:
        return None
    return Artist(**result)


def create_artist_from_name(conn: Connection, name: str) -> Artist:
    sql = """
    insert into example.artist (name)
    values (:name)
    """
    params = {"name": name}
    conn.execute(text(sql), params)
    artist = get_artist_from_name(conn, name)
    if artist is None:
        raise ValueError(f"Unable to successfully create artist for {name}")
    return artist
