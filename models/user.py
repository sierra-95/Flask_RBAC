from sqlalchemy import Column, Integer, String
from flask_login import UserMixin
from .basemodel import Base
from db_engine import db

class User(db.Model, UserMixin, Base):
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    roles = db.relationship('Role', secondary='user_roles')
