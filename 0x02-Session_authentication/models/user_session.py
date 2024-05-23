#!/usr/bin/env python3
"""class that inherits from Base"""


from api.v1.auth.auth import Auth
from api.v1.auth.session_auth import SessionAuth
from models.user import User
from os import getenv
from models.base import Base


class UserSession(Base):
    """Session ID stored in database"""
    def __init__(self, *args: list, **kwargs: dict):
        """store session and id for users"""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
