import uuid

from flask import Blueprint, request

from webapp.daos import artist_dao
from webapp.database import engine

blueprint = Blueprint("artist", __name__, url_prefix="/artist")


@blueprint.route("/", methods=["GET"])
def get_all_artists():
    with engine.connect() as conn:
        artists = artist_dao.get_all_artists(conn)
    return [artist.model_dump() for artist in artists]
