from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class Swimmer(Base):
    __tablename__ = 'swimmers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    team = Column(String)

    
    results = relationship("SwimResult", back_populates="swimmer", cascade="all, delete")

    def __repr__(self):
        return f"<Swimmer(id={self.id}, name='{self.name}', team='{self.team}')>"
