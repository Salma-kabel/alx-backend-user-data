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
