from models.base import session
from models.swimmer import Swimmer
from models.swim_result import SwimResult

def main_menu():
    while True:
        print(" Welcome to AquaTrack ")
        print("1. View all swimmers")
        print("2. Add a new swimmer")
        print("3. Delete a swimmer")
        print("4. View swimmer results")
        print("5. Add swim result")
        print("6. Exit")

        choice = input("Enter your choice (1–6): ")

        if choice == "1":
            view_all_swimmers()
        elif choice == "2":
            add_swimmer()
        elif choice == "3":
            delete_swimmer()
        elif choice == "4":
            view_results()
        elif choice == "5":
            add_result()
        elif choice == "6":
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


def view_all_swimmers():
    swimmers = session.query(Swimmer).all()
    if not swimmers:
        print("No swimmers found.")
    for swimmer in swimmers:
        print(f"{swimmer.id}: {swimmer.name} (Age: {swimmer.age}, Team: {swimmer.team})")

def add_swimmer():
    name = input("Enter swimmer name: ")
    age = input("Enter age: ")
    team = input("Enter team: ")

    if not age.isdigit():
        print("Age must be a number.")
        return

    swimmer = Swimmer(name=name, age=int(age), team=team)
    session.add(swimmer)
    session.commit()
    print(f"Swimmer '{name}' added successfully!")

def delete_swimmer():
    view_all_swimmers()
    id = input("Enter the ID of the swimmer to delete: ")
    swimmer = session.query(Swimmer).get(id)

    if swimmer:
        session.delete(swimmer)
        session.commit()
        print(f"Swimmer '{swimmer.name}' deleted.")
    else:
        print("Swimmer not found.")

def view_results():
    view_all_swimmers()
    id = input("Enter swimmer ID to view their results: ")
    swimmer = session.query(Swimmer).get(id)

    if swimmer:
        print(f"\nResults for {swimmer.name}:")
        if swimmer.results:
            for result in swimmer.results:
                print(f"- {result.event}: {result.time}s at {result.meet_name}")
        else:
            print("No results found.")
    else:
        print("Swimmer not found.")

def add_result():
    view_all_swimmers()
    id = input("Enter swimmer ID to add a result: ")
    swimmer = session.query(Swimmer).get(id)

    if swimmer:
        event = input("Enter event name (e.g. '100m Freestyle'): ")
        time = input("Enter time (in seconds): ")
        meet = input("Enter meet name: ")

        try:
            time = float(time)
        except ValueError:
            print("Time must be a number.")
            return

        result = SwimResult(event=event, time=time, meet_name=meet, swimmer=swimmer)
        session.add(result)
        session.commit()
        print(f"Result added for {swimmer.name}!")
    else:
        print("Swimmer not found.")

if __name__ == "__main__":
    main_menu()
