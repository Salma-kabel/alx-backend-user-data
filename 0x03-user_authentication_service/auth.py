#!/usr/bin/env python3
"""auth file script"""


from db import DB
from typing import TypeVar
from user import User
import bcrypt
from uuid import uuid4
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """takes in a password string arguments and returns bytes"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """return a User object"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError("User "+ email + " already exists")
        except Exception:
            pwd = _hash_password(password)
            user = self._db.add_user(email, pwd)
            return user