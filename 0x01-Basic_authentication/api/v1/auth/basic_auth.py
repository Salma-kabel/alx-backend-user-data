#!/usr/bin/env python3
"""class basic auth that inherits from auth"""


from flask import request
from tabnanny import check
from flask import request
from typing import TypeVar, List
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """class that inherits from Auth"""
