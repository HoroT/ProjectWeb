from flask import render_template

from . import index_bp


@index_bp.route("/")
@index_bp.route("/index.html")
def index():
    return render_template("index.html")
