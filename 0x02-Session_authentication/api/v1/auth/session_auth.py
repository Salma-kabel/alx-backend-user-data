#!/usr/bin/env python3
"""class SessionAuth that inherits from Auth"""


from api.v1.auth.auth import Auth
from typing import TypeVar, List
from models.user import User
import base64
import uuid


class SessionAuth(Auth):
    """ the first step for creating a new authentication mechanism"""
    user_id_by_session_id = {}
    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id"""
        if user_id is None or type(user_id) is not str:
            return None
        else:
            session_id = kwargs.get('id', str(uuid.uuid4()))
            user_id_by_session_id[session_id] = user_id
            return session_id

