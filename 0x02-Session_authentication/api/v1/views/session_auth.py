#!/usr/bin/env python3
"""session authentication views"""


from flask import request, jsonify, abort
from api.v1.views import app_views
from models.user import User
from os import getenv
from flask import make_response


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def login():
    """handles all routes for the Session authentication"""
    email = request.form.get("email")
    pwd = request.form.get("password")
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not pwd:
        return jsonify({"error": "password missing"}), 400
    try:
        users = User.search({"email": email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404
    if not users:
        return jsonify({"error": "no user found for this email"}), 404
    for user in users:
        if user.is_valid_password(pwd):
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            res = make_response(user.to_json())
            res.set_cookie(getenv("SESSION_NAME"), session_id)
            return res
        else:
            return jsonify({"error": "wrong password"}), 401
    return jsonify({"error": "no user found for this email"}), 404


@app_views.route("/auth_session/logout",
                 methods=["DELETE"], strict_slashes=False)
def logout():
    """logout the user"""
    from api.v1.app import auth
    if auth.destroy_session(request):
        return jsonify({}), 200
    else:
        abort(404)
