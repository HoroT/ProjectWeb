from flask import Blueprint

index_bp = Blueprint(name="index", url_prefix="/", import_name=__name__)
from . import routes  # noqa: E402
