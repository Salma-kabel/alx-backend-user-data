#!/usr/bin/env python3
"""class basic auth that inherits from auth"""


from flask import request
from tabnanny import check
from flask import request
from typing import TypeVar, List
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """class that inherits from Auth"""
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """returns the Base64 part of the Authorization"""
        if (authorization_header is None or
                type(authorization_header) is not str or
                not authorization_header.startswith("Basic")):
            return None
        return authorization_header[6:]
