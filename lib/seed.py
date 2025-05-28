from models.base import session
from models.swimmer import Swimmer
from models.swim_result import SwimResult

session.query(SwimResult).delete()
session.query(Swimmer).delete()

swimmer1 = Swimmer(name="Elaine Buyeke", age=18, team="Blue Sharks")
swimmer2 = Swimmer(name="Tyra Mwai", age=18, team="Wave Warriors")

result1 = SwimResult(event="100m Freestyle", time=58.5, meet_name="City Meet", swimmer=swimmer1)
result2 = SwimResult(event="50m Backstroke", time=31.2, meet_name="State Champs", swimmer=swimmer1)
result3 = SwimResult(event="200m IM", time=142.3, meet_name="Regional Finals", swimmer=swimmer2)

session.add_all([swimmer1, swimmer2, result1, result2, result3])

session.commit()

print("Seed data inserted successfully!")
