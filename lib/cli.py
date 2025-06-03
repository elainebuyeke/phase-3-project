from helpers import (
    get_all_swimmers,
    find_swimmer_by_id,
    create_swimmer,
    delete_swimmer,
    get_all_results,
    create_result,
    is_positive_int,
    print_error,
    print_success,
)

def main_menu():
    while True:
        print("Welcome to AquaTrack ")
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
            delete_swimmer_menu()
        elif choice == "4":
            view_results()
        elif choice == "5":
            add_result()
        elif choice == "6":
            print("Goodbye!")
            exit()
        else:
            print_error("Invalid choice. Please enter a number between 1 and 6.")

def view_all_swimmers():
    swimmers = get_all_swimmers()
    if not swimmers:
        print("No swimmers found.")
    else:
        for s in swimmers:
            print(f"{s.id}: {s.name} (Age: {s.age}, Team: {s.team})")

def add_swimmer():
    name = input("Enter swimmer name: ")
    age = input("Enter age: ")
    team = input("Enter team: ")

    if not is_positive_int(age):
        print_error("Age must be a positive number.")
        return

    swimmer = create_swimmer(name, int(age), team)
    print_success(f"Swimmer '{swimmer.name}' added successfully!")

def delete_swimmer_menu():
    view_all_swimmers()
    id = input("Enter the ID of the swimmer to delete: ")

    if not is_positive_int(id):
        print_error("ID must be a positive number.")
        return

    swimmer = find_swimmer_by_id(int(id))
    if swimmer:
        delete_swimmer(swimmer)
        print_success(f"Swimmer '{swimmer.name}' deleted.")
    else:
        print_error("Swimmer not found.")

def view_results():
    view_all_swimmers()
    id = input("Enter swimmer ID to view their results: ")

    if not is_positive_int(id):
        print_error("ID must be a positive number.")
        return

    swimmer = find_swimmer_by_id(int(id))
    if swimmer:
        print(f"\nResults for {swimmer.name}:")
        if swimmer.results:
            for result in swimmer.results:
                print(f"- {result.event}: {result.time}s at {result.meet_name}")
        else:
            print("No results found.")
    else:
        print_error("Swimmer not found.")

def add_result():
    view_all_swimmers()
    id = input("Enter swimmer ID to add a result: ")

    if not is_positive_int(id):
        print_error("ID must be a positive number.")
        return

    swimmer = find_swimmer_by_id(int(id))
    if swimmer:
        event = input("Enter event name (e.g. '100m Freestyle'): ")
        time = input("Enter time (in seconds): ")
        meet = input("Enter meet name: ")

        try:
            time_val = float(time)
        except ValueError:
            print_error("Time must be a number.")
            return

        create_result(event, time_val, meet, swimmer)
        print_success(f"Result added for {swimmer.name}!")
    else:
        print_error("Swimmer not found.")

if __name__ == "__main__":
    main_menu()
