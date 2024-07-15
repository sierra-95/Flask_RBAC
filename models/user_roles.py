from sqlalchemy import Column, Integer, ForeignKey
from .basemodel import Base
from db_engine import db

class UserRoles(db.Model, Base):
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    role_id = Column(Integer, ForeignKey('role.id'), primary_key=True)
