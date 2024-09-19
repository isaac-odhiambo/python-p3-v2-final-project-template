from helpers import (
    exit_program,
    list_departments,
    find_department_by_name,
    find_department_by_id,
    create_department,
    update_department,
    delete_department,
    list_staff,
    find_staff_by_name,
    find_staff_by_id,
    create_staff,
    update_staff,
    delete_staff,
    list_staff_in_department,
    list_rooms,
    find_room_by_number,
    create_room,
    update_room,
    delete_room,
    list_reservations,
    find_reservation_by_id,
    create_reservation,
    update_reservation,
    delete_reservation,
    list_orders,
    find_order_by_id,
    create_order,
    update_order,
    delete_order
)

# Dummy credentials for demonstration
credentials = {
    "Manager": "1234",
    "Staff": "1234"
}

def main():
    role = authenticate_user()
    while True:
        menu(role)
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif role == "Manager":
            handle_manager_choices(choice)
        elif role == "Staff":
            handle_staff_choices(choice)
        elif role == "Guest":
            handle_guest_choices(choice)
        else:
            print("Invalid role")

def authenticate_user():
    print("Enter your role (Manager/Staff/Guest): ")
    role = input("> ").strip().capitalize()
    
    if role in ["Manager", "Staff"]:
        password = input("Enter your password: ")
        if password != credentials[role]:
            print("Invalid password. Defaulting to Guest.")
            role = "Guest"
    elif role not in ["Guest"]:
        print("Invalid role. Defaulting to Guest.")
        role = "Guest"
        
    return role

def menu(role):
    print("Please select an option:")
    print("0. Exit the program")
    
    if role in ["Manager", "Staff"]:
        print("1. List all departments")
        print("2. Find department by name")
        print("3. Find department by id")
        if role == "Manager":
            print("4. Create department")
            print("5. Update department")
            print("6. Delete department")
        print("7. List all staff")
        print("8. Find staff by name")
        print("9. Find staff by id")
        if role == "Manager":
            print("10. Create staff")
            print("11. Update staff")
            print("12. Delete staff")
        print("13. List all staff in a department")
        print("16. List rooms")
        print("17. Find room by number")
        if role == "Manager":
            print("18. Create room")
            print("19. Update room")
            print("20. Delete room")
        print("21. List reservations")
        print("22. Find reservation by id")
        if role == "Manager":
            print("23. Update reservation")
            print("24. Delete reservation")
        print("25. List orders")
        print("26. Find order by id")
        if role == "Manager":
            print("27. Create order")
            print("28. Update order")
            print("29. Delete order")
    elif role == "Guest":
        print("14. Book a room")
        print("16. List rooms")  # Guests can also view rooms

def handle_manager_choices(choice):
    if choice == "1":
        list_departments()
    elif choice == "2":
        find_department_by_name()
    elif choice == "3":
        find_department_by_id()
    elif choice == "4":
        create_department()
    elif choice == "5":
        update_department()
    elif choice == "6":
        delete_department()
    elif choice == "7":
        list_staff()
    elif choice == "8":
        find_staff_by_name()
    elif choice == "9":
        find_staff_by_id()
    elif choice == "10":
        create_staff()
    elif choice == "11":
        update_staff()
    elif choice == "12":
        delete_staff()
    elif choice == "13":
        list_staff_in_department()
    elif choice == "16":
        list_rooms()
    elif choice == "17":
        find_room_by_number()
    elif choice == "18":
        create_room()
    elif choice == "19":
        update_room()
    elif choice == "20":
        delete_room()
    elif choice == "21":
        list_reservations()
    elif choice == "22":
        find_reservation_by_id()
    elif choice == "23":
        update_reservation()
    elif choice == "24":
        delete_reservation()
    elif choice == "25":
        list_orders()
    elif choice == "26":
        find_order_by_id()
    elif choice == "27":
        create_order()
    elif choice == "28":
        update_order()
    elif choice == "29":
        delete_order()
    else:
        print("Invalid choice")

def handle_staff_choices(choice):
    if choice == "1":
        list_departments()
    elif choice == "2":
        find_department_by_name()
    elif choice == "3":
        find_department_by_id()
    elif choice == "7":
        list_staff()
    elif choice == "8":
        find_staff_by_name()
    elif choice == "9":
        find_staff_by_id()
    elif choice == "13":
        list_staff_in_department()
    elif choice == "16":
        list_rooms()
    elif choice == "17":
        find_room_by_number()
    elif choice == "21":
        list_reservations()
    elif choice == "22":
        find_reservation_by_id()
    elif choice == "25":
        list_orders()
    elif choice == "26":
        find_order_by_id()
    else:
        print("Invalid choice")

def handle_guest_choices(choice):
    if choice == "14":
        create_reservation()
    elif choice == "16":
        list_rooms()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
