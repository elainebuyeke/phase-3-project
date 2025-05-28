from models.base import session
from models.swimmer import Swimmer
from models.swim_result import SwimResult


def get_all_swimmers():
    return session.query(Swimmer).all()

def find_swimmer_by_id(swimmer_id):
    return session.query(Swimmer).get(swimmer_id)

def create_swimmer(name, age, team):
    swimmer = Swimmer(name=name, age=age, team=team)
    session.add(swimmer)
    session.commit()
    return swimmer

def delete_swimmer(swimmer):
    session.delete(swimmer)
    session.commit()


def get_all_results():
    return session.query(SwimResult).all()

def find_result_by_id(result_id):
    return session.query(SwimResult).get(result_id)

def create_result(event, time, meet_name, swimmer):
    result = SwimResult(event=event, time=time, meet_name=meet_name, swimmer=swimmer)
    session.add(result)
    session.commit()
    return result

def delete_result(result):
    session.delete(result)
    session.commit()


def is_positive_int(value):
    return value.isdigit() and int(value) > 0

def print_error(message):
    print(f"{message}")

def print_success(message):
    print(f"{message}")
