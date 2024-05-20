#!/usr/bin/env python3
"""class to manage the API authentication"""


from flask import request
from tabnanny import check
from flask import request
from typing import TypeVar, List


class Auth:
    """class to manage api"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns path and excluded_paths"""
        if path is None:
            return True
        if path in excluded_paths or (path + '/') in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Flask request object"""
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """will be the Flask request object"""
        return None
