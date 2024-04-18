from flask import Blueprint

blueprint = Blueprint("health", __name__, url_prefix="/health")


@blueprint.route("/", methods=["GET"])
def up():
    """Simple route to ensure that the application is accessible"""
    return "Running up that hill"
