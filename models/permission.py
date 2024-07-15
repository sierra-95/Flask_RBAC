from sqlalchemy import Column, Integer, String
from .basemodel import Base
from db_engine import db

class Permission(db.Model, Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(String(255))
