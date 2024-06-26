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
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a User ID based on a Session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """returns a User instance based on a cookie value"""
        session_id = self.session_cookie(request)
        uid = self.user_id_for_session_id(session_id)
        return User.get(uid)

    def destroy_session(self, request=None):
        """deletes the user session"""
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id:
            user = self.user_id_for_session_id(session_id)
            if user:
                del self.user_id_by_session_id[session_id]
                return True
        return False
