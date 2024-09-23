# lib/helpers.py
from models.department import Department
from models.staff import Staff
from models.room import Room
from models.reservation import Reservation
from models.order import Order

def exit_program():
    print("Goodbye!")
    exit()

# Department functions
def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)

def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(f'Department {name} not found')

def find_department_by_id():
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')

def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)

def update_department():
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    if department:
        try:
            name = input("Enter the department's new name: ")
            location = input("Enter the department's new location: ")
            department.name = name
            department.location = location
            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')

def delete_department():
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    if department:
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')

# Staff functions
def list_staff():
    staff_members = Staff.get_all()
    for staff in staff_members:
        print(staff)

def find_staff_by_name():
    name = input("Enter the staff member's name: ").strip().lower()
    staff_members = Staff.get_all()
    matching_staff = [staff for staff in staff_members if staff.name.lower() == name]
    
    if matching_staff:
        print(f"Found {len(matching_staff)} staff member(s) with the name '{name}':")
        for staff in matching_staff:
            print(staff)
    else:
        print(f"No staff member found with the name '{name}'")

def find_staff_by_id():
    id_ = input("Enter the staff member's id: ")
    staff = Staff.find_by_id(id_)
    print(staff) if staff else print(f'Staff member {id_} not found')

def create_staff():
    name = input("Enter the staff member's name: ")
    job_title = input("Enter the staff member's job title: ")
    try:
        department_id = int(input("Enter the staff member's department id: "))
        staff = Staff.create(name, job_title, department_id)
        print(f'Success: {staff}')
    except ValueError:
        print("Error: department_id must be an integer.")
    except Exception as exc:
        print(f"Error creating staff member: {exc}")

def update_staff():
    id_ = input("Enter the staff member's id: ")
    staff = Staff.find_by_id(id_)
    if staff:
        try:
            name = input("Enter the staff member's new name: ")
            staff.name = name
            job_title = input("Enter the staff member's new job title: ")
            staff.job_title = job_title
            department_id = int(input("Enter the staff member's new department id: "))
            staff.department_id = department_id
            staff.update()
            print(f'Success: {staff}')
        except ValueError:
            print("Error: department_id must be an integer.")
        except Exception as exc:
            print(f"Error updating staff member: {exc}")
    else:
        print(f'Staff member {id_} not found')

def delete_staff():
    id_ = input("Enter the staff member's id: ")
    staff = Staff.find_by_id(id_)
    if staff:
        staff.delete()
        print(f'Staff member {id_} deleted')
    else:
        print(f'Staff member {id_} not found')

def list_staff_in_department():
    department_id = int(input("Enter the department's id: "))
    staff_members = Staff.find_by_department_id(department_id)
    
    if staff_members:
        for staff in staff_members:
            print(staff)
    else:
        print(f'No staff members found in department {department_id}')

# Room functions
def list_rooms():
    rooms = Room.get_all()
    for room in rooms:
        print(room)

def find_room_by_number():
    number = input("Enter the room number: ")
    room = Room.find_by_number(number)
    print(room) if room else print(f'Room {number} not found')

def create_room():
    number = input("Enter the room number: ")
    room_type = input("Enter the room type: ")
    price = float(input("Enter the room price: "))
    try:
        room = Room.create(number, room_type, price)
        print(f'Success: {room}')
    except Exception as exc:
        print("Error creating room: ", exc)

def update_room():
    number = input("Enter the room number: ")
    room = Room.find_by_number(number)
    if room:
        try:
            room_type = input("Enter the new room type: ")
            room.room_type = room_type
            price = float(input("Enter the new room price: "))
            room.price = price
            room.update()
            print(f'Success: {room}')
        except Exception as exc:
            print("Error updating room: ", exc)
    else:
        print(f'Room {number} not found')

def delete_room():
    number = input("Enter the room number: ")
    room = Room.find_by_number(number)
    if room:
        room.delete()
        print(f'Room {number} deleted')
    else:
        print(f'Room {number} not found')

# Reservation functions
def list_reservations():
    reservations = Reservation.get_all()
    for reservation in reservations:
        print(reservation)

def find_reservation_by_id():
    id_ = input("Enter the reservation's id: ")
    reservation = Reservation.find_by_id(id_)
    print(reservation) if reservation else print(f'Reservation {id_} not found')

def create_reservation():
    room_number = input("Enter the room number: ")
    guest_name = input("Enter the guest's name: ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    staff_id = input("Enter the staff member's id: ")
    department_id = input("Enter the department's id: ")
    try:
        room = Room.find_by_number(room_number)
        reservation = Reservation.create(room_id=room.id, guest_name=guest_name, start_date=start_date, end_date=end_date, staff_id=staff_id, department_id=department_id)
        print(f'Success: {reservation}')
    except Exception as exc:
        print("Error creating reservation: ", exc)

def update_reservation():
    id_ = input("Enter the reservation's id: ")
    reservation = Reservation.find_by_id(id_)
    if reservation:
        try:
            room_number = input("Enter the new room number: ")
            room = Room.find_by_number(room_number)
            guest_name = input("Enter the new guest name: ")
            start_date = input("Enter the new start date (YYYY-MM-DD): ")
            end_date = input("Enter the new end date (YYYY-MM-DD): ")
            staff_id = input("Enter the new staff member's id: ")
            department_id = input("Enter the new department's id: ")

            reservation.room_id = room.id
            reservation.guest_name = guest_name
            reservation.start_date = start_date
            reservation.end_date = end_date
            reservation.staff_id = staff_id
            reservation.department_id = department_id
            reservation.update()
            print(f'Success: {reservation}')
        except Exception as exc:
            print("Error updating reservation: ", exc)
    else:
        print(f'Reservation {id_} not found')

def delete_reservation():
    id_ = input("Enter the reservation's id: ")
    reservation = Reservation.find_by_id(id_)
    if reservation:
        reservation.delete()
        print(f'Reservation {id_} deleted')
    else:
        print(f'Reservation {id_} not found')

# Order functions
def list_orders():
    orders = Order.get_all()
    for order in orders:
        print(order)

def find_order_by_id():
    id_ = input("Enter the order's id: ")
    order = Order.find_by_id(id_)
    print(order) if order else print(f'Order {id_} not found')

def create_order():
    room_number = input("Enter the room number: ")
    guest_name = input("Enter the guest's name: ")  # Prompt for guest name
    quantity = int(input("Enter the quantity: "))
    total_price = float(input("Enter the total price: "))
    
    try:
        room = Room.find_by_number(room_number)
        if room:
            order = Order.create(room_id=room.id, quantity=quantity, guest_name=guest_name, total_price=total_price)
            print(f'Success: {order}')
        else:
            print(f'Room {room_number} not found.')
    except Exception as exc:
        print("Error creating order: ", exc)

def update_order():
    id_ = input("Enter the order's id: ")
    order = Order.find_by_id(id_)
    if order:
        try:
            room_number = input("Enter the new room number: ")
            room = Room.find_by_number(room_number)
            if room:
                order.room_id = room.id
                order.quantity = int(input("Enter the new quantity: "))
                order.guest_name = input("Enter the new guest name: ")  # Prompt for new guest name
                order.total_price = float(input("Enter the new total price: "))
                order.update()
                print(f'Success: {order}')
            else:
                print(f'Room {room_number} not found.')
        except Exception as exc:
            print("Error updating order: ", exc)
    else:
        print(f'Order {id_} not found')

def delete_order():
    id_ = input("Enter the order's id: ")
    order = Order.find_by_id(id_)
    if order:
        order.delete()
        print(f'Order {id_} deleted')
    else:
        print(f'Order {id_} not found')
