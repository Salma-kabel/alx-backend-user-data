#!/usr/bin/env python3
"""class basic auth that inherits from auth"""


from api.v1.auth.auth import Auth
from typing import TypeVar, List
from models.user import User
import base64
import binascii


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """returns the decoded value of a Base64
        string base64_authorization_header"""
        if (base64_authorization_header is None or
                type(base64_authorization_header) is not str):
            return None
        try:
            base = base64_authorization_header
            return base64.b64decode(base).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ returns the user email and password
        from the Base64 decoded value"""
        if (decoded_base64_authorization_header is None or
                type(decoded_base64_authorization_header) is not str
                or ':' not in decoded_base64_authorization_header):
            return (None, None)
        headr = decoded_base64_authorization_header
        return (headr.split(":")[0], headr.split(":")[1])

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on his email and password"""
        if (user_email is None or type(user_email) is not str or
                user_pwd is None or type(user_pwd) is not str):
            return None
        users = User.search({'email': user_email})
        if not users:
            return None
        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user
