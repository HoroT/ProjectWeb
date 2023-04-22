from flask import Blueprint

map_bp = Blueprint(name="map", url_prefix="/map", import_name=__name__)
from . import routes  # noqa: E402
