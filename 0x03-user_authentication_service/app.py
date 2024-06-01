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
def login() -> str:
    """implement a login function to respond
    to the POST /sessions route"""
    email = request.form.get("email")
    password = request.form.get("password")
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        res = jsonify({"email": f"{email}", "message": "logged in"})
        res.set_cookie("session_id", session_id)
        return res
    else:
        abort(401)


@app.route("/sessions", methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """ destroy the session and redirect the user to GET /.
    If the user does not exist, respond with a 403"""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    else:
        abort(403)


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile() -> str:
    """ find the user. If the user exist, respond with a
    200 HTTP status and the following JSON payload"""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


@app.route("/reset_password", methods=["POST"], strict_slashes=False)
def get_reset_password_token() -> str:
    """If the email is not registered, respond with a 403 status code
    Otherwise, generate a token and respond with a 200 HTTP status"""
    email = request.form.get('email')
    session_id = AUTH.create_session(email)
    if session_id:
        return jsonify({"email": email, "reset_token": session_id}), 200
    else:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password() -> str:
    """ PUT /reset_password
      Return:
        - message
    """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_psw = request.form.get('new_password')
    try:
        AUTH.update_password(reset_token, new_psw)
        return jsonify({"email": f"{email}",
                        "message": "Password updated"}), 200
    except NoResultFound:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
