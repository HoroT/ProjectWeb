from flask import jsonify, render_template, request
from flask_login import current_user, login_required

from . import map_bp
from vdmap.extensions import map_, rc, d
from vdmap.db.models.routes import Routes


@map_bp.route("/")
@login_required
def m():
    return render_template("map.html", user=current_user.email,
                           pavilions=map_.get_pavilions(serialized=False), saved_routes=current_user.get_routes())


@map_bp.route("/get_points")
@login_required
def get_points():
    return jsonify({"pavilions": map_.get_pavilions(), "center": map_.center.serialize()})


@map_bp.route("/build_route")
@login_required
def build_route():
    p, tm = rc.generate_route(request.args.getlist("p1[]"), request.args.getlist("p2[]"))
    if p is None:
        return jsonify({"error": "error"})
    return jsonify({"ok": "ok", "route": p, "time": tm})


@map_bp.route("/save_route", methods=["POST"])
@login_required
def save_route():
    j = request.json
    n1 = j.get("n1", None)
    n2 = j.get("n2", None)
    p1 = j.get("p1", None)
    p2 = j.get("p2", None)
    if not all([n1, n2, p1, p2]):
        return jsonify({"error": "bad-data"})
    name = f"{n1} -> {n2}"
    route = Routes()
    route.user_id = current_user.id
    route.set_route(name, p1, p2)
    print( route )
    with d() as db:
        db.add(route)
        db.commit()
        print( db )
    return jsonify({"ok": "ok"})


@map_bp.route("/get_saved_routes")
@login_required
def get_saved_routes():
    u = current_user
    return u.get_routes()
