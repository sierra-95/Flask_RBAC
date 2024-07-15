from sqlalchemy import Column, Integer, ForeignKey
from .basemodel import Base
from db_engine import db

class RolePermissions(db.Model, Base):
    role_id = Column(Integer, ForeignKey('role.id'), primary_key=True)
    permission_id = Column(Integer, ForeignKey('permission.id'), primary_key=True)
