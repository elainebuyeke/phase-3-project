from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class SwimResult(Base):
    __tablename__ = 'swim_results'

    id = Column(Integer, primary_key=True)
    event = Column(String)
    time = Column(Float)
    meet_name = Column(String)

    swimmer_id = Column(Integer, ForeignKey('swimmers.id'))
    swimmer = relationship("Swimmer", back_populates="results")

    def __repr__(self):
        return f"<Result: {self.event} - {self.time}s at {self.meet_name}>"
