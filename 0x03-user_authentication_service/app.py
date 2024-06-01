#!/usr/bin/env python3
"""set up a basic Flask app"""


from auth import Auth
from flask import Flask, jsonify, request, abort, redirect


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    return jsonify({"message": "Bienvenue"}), 200


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    """ the end-point to register a user."""
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": f"email", "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
    """ implement a login function to respond
    to the POST /sessions route"""
def login() -> str:
    email = request.form.get("email")
    password = request.form.get("password")
    valid_login = AUTH.valid_login(email, password)
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        res = jsonify({"email": f"{email}", "message": "logged in"})
        res.set_cookie("session_id", session_id)
        return res
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
