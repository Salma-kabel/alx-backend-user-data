#!/usr/bin/env python3
"""create a SQLAlchemy model named User for
a database table named users"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """"""
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=False)
    reset_token = Column(String(250), nullable=False)

    def __repr__(self):
        """String representation"""
        return f"User: id={self.id}"
