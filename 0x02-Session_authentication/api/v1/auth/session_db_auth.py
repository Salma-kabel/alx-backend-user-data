#!/usr/bin/env python3
"""new authentication class SessionDBAuth"""


from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from flask import request
from models.base import Base
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """class inherits from SessionExpAuth"""
    user_id_by_session_id = {}

    def create_session(self, user_id=None):
        """creates and stores new instance of
        UserSession and returns the Session ID"""
        if user_id is None:
            return None
        session = UserSession(user_id=user_id)
        session.session_id = session.id
        session.save()
        return session.session_id

    def user_id_for_session_id(self, session_id=None):
        """ returns the User ID by requesting
        UserSession in the database based on session_id"""
        
        if session_id is None:
            return None
        try:
            sessions = UserSession.search({'session_id': session_id})
        except Exception:
            return None
        if not sessions:
            return None
        session = sessions[0]
        return session.user_id

    def destroy_session(self, request=None):
        """destroys the UserSession based on the
        Session ID from the request cookie"""
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id:
            session = UserSession.get(session_id)
            if session:
                session.remove()
                return True
        return False
