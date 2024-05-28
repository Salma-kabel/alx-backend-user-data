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
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
