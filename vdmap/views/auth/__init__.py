from flask import Blueprint

auth_bp = Blueprint(name="auth", url_prefix="/auth", import_name=__name__)
from . import routes  # noqa: E402
