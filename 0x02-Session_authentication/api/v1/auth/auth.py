#!/usr/bin/env python3
"""class to manage the API authentication"""


from flask import request
from tabnanny import check
from typing import TypeVar, List
from os import getenv


class Auth:
    """class to manage api auth"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns none-path and excluded_paths"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        for ex_path in excluded_paths:
            if ex_path[-1] == "*":
                if path.startswith(ex_path[:-1]):
                    return False
        if path in excluded_paths or (path + '/') in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Flask request object return none-header"""
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """will be the Flask request object return none"""
        return None

    def session_cookie(self, request=None):
        """returns a cookie value from a request"""
        if request is None:
            return None
        session_name = getenv('SESSION_NAME')
        return request.cookies.get(session_name)
