from flask import jsonify, render_template, request, url_for
from flask_login import login_user, logout_user, login_required

from . import auth_bp
from vdmap import d
from vdmap.db.models.users import Users


@auth_bp.route("/login", methods=["POST"])
def login():
    email, password = request.form.get("email", None), request.form.get("password")
    if None in [email, password]:
        return jsonify({"error": "no-data"})
    with d() as db:
        u: Users = db.query(Users).filter(Users.email == email).first()
        if u is None:
            return jsonify({"error": "no-user"})
        if not u.check_password(password):
            return jsonify({"error": "wrong-password"})
        login_user(u)
    return jsonify({"ok": "ok", "redirect": url_for("map.m")})


@auth_bp.route("/register", methods=["POST"])
def register():
    email, password = request.form.get("email", None), request.form.get("password")
    if None in [email, password]:
        return jsonify({"error": "no-data"})
    u = Users(email=email)
    u.set_password(password)
    with d() as db:
        db.add(u)
        db.commit()
    return jsonify({"ok": "ok"})


@auth_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"ok": "ok"})
