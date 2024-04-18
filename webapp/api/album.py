import uuid

from flask import Blueprint, request

from webapp.models.album import Album
from webapp.orchestrators import album_orchestrator

blueprint = Blueprint("album", __name__, url_prefix="/album")


@blueprint.route("/create", methods=["POST"])
def create_album():
    """Simple route to ensure that the application is accessible"""
    req = Album(id=str(uuid.uuid4()), **request.get_json())
    album_orchestrator.create(req)
    return req.model_dump()
