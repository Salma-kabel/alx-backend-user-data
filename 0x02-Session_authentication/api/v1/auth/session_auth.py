#!/usr/bin/env python3
"""class SessionAuth that inherits from Auth"""


from api.v1.auth.auth import Auth
from typing import TypeVar, List
from models.user import User
import base64


class SessionAuth(Auth):
    """ the first step for creating a new authentication mechanism"""
