#!/usr/bin/env python3
"""session expiration auth"""


from api.v1.auth.auth import Auth
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
from models.user import User
from os import getenv


class SessionExpAuth(SessionAuth):
    """add an expiration date to a Session ID"""
    def __init__(self):
        """Assign an instance attribute session_duration"""
        self.session_duration = int(getenv('SESSION_DURATION', 0))

    def create_session(self, user_id=None):
        """Create a Session ID by calling super()"""
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_dictionary = {"user_id": user_id, "created_at": datetime.now()}
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Return None if session_id is None"""
        if session_id is None:
            return None
        session_dictionary = self.user_id_by_session_id.get(session_id)
        if session_dictionary:
            user_id = session_dictionary.get('user_id')
            if self.session_duration <= 0:
                return user_id
            created = session_dictionary.get('created_at')
            if created:
                if created + timedelta(seconds=self.session_duration) < datetime.now():
                    return None
                return user_id
        return None
