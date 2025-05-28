from models.base import Base, engine
from models import swimmer, swim_result 

Base.metadata.create_all(engine)

print("Database and tables created!")
