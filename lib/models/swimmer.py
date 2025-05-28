from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Swimmer(Base):
    __tablename__ = 'swimmers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    team = Column(String)

results = relationship("SwimResult", back_populates="swimmer", cascade="all, delete-orphan")