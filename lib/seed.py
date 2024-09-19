from models.__init__ import CONN, CURSOR
from models.department import Department
from models.staff import Staff
from models.room import Room
from models.reservation import Reservation
from models.order import Order

def initialize_database():
    # Drop existing tables to reset the database
    Order.drop_table()
    Reservation.drop_table()
    Room.drop_table()
    Staff.drop_table()
    Department.drop_table()

    # Create new tables
    Department.create_table()
    Staff.create_table()
    Room.create_table()
    Reservation.create_table()
    Order.create_table()

    # Create Departments
    front_desk = Department.create(name="Front Desk", location="Ground Floor")
    housekeeping = Department.create(name="Housekeeping", location="First Floor")
    kitchen = Department.create(name="Kitchen", location="Basement")
    management = Department.create(name="Management", location="Second Floor")
    maintenance = Department.create(name="Maintenance", location="Ground Floor")

    # Create Staff Members
    staff_1 = Staff.create(name="Awino Connie", job_title="Receptionist", department_id=front_desk.id)
    staff_2 = Staff.create(name="Neremy Eunice", job_title="Housekeeper", department_id=housekeeping.id)
    staff_3 = Staff.create(name="Ephy Wakesa", job_title="Chef", department_id=kitchen.id)
    staff_4 = Staff.create(name="Isaac Odhiambo", job_title="Manager", department_id=management.id)
    staff_5 = Staff.create(name="Evan Kiprono", job_title="Maintenance Worker", department_id=maintenance.id)

    # Create Rooms
    room_1 = Room.create(room_number="101", room_type="Single", price=100)
    room_2 = Room.create(room_number="102", room_type="Double", price=150)
    room_3 = Room.create(room_number="103", room_type="Suite", price=250)
    room_4 = Room.create(room_number="104", room_type="Penthouse", price=500)
    room_5 = Room.create(room_number="105", room_type="Deluxe", price=300)

    # Create Reservations
    reservation_1 = Reservation.create(
        room_id=room_1.id, 
        guest_name="Cecile Mwangi", 
        start_date="2024-09-20", 
        end_date="2024-09-25", 
        staff_id=staff_1.id, 
        department_id=front_desk.id
    )
    reservation_2 = Reservation.create(
        room_id=room_2.id, 
        guest_name="Alicia Manu", 
        start_date="2024-09-21", 
        end_date="2024-09-26", 
        staff_id=staff_1.id, 
        department_id=front_desk.id
    )
    reservation_3 = Reservation.create(
        room_id=room_3.id, 
        guest_name="Janet Atsa", 
        start_date="2024-09-18", 
        end_date="2024-09-22", 
        staff_id=staff_2.id, 
        department_id=housekeeping.id
    )
    reservation_4 = Reservation.create(
        room_id=room_4.id, 
        guest_name="Wicklife Omondi", 
        start_date="2024-09-19", 
        end_date="2024-09-23", 
        staff_id=staff_3.id, 
        department_id=kitchen.id
    )
    reservation_5 = Reservation.create(
        room_id=room_5.id, 
        guest_name="Goddfrey Atsa", 
        start_date="2024-09-20", 
        end_date="2024-10-24", 
        staff_id=staff_4.id, 
        department_id=management.id
    )

    # Create Orders
    order_1 = Order.create(
        room_id=room_1.id, 
        staff_id=staff_3.id, 
        guest_name="Alicia "
    )
    order_2 = Order.create(
        room_id=room_2.id, 
        staff_id=staff_3.id, 
        guest_name="Jane Atsa"
    )
    order_3 = Order.create(
        room_id=room_3.id, 
        staff_id=staff_2.id, 
        guest_name="Wicklife Omondi"
    )
    order_4 = Order.create(
        room_id=room_4.id, 
        staff_id=staff_4.id, 
        guest_name="Cecile Mwangi"
    )
    order_5 = Order.create(
        room_id=room_5.id, 
        staff_id=staff_5.id, 
        guest_name="Goddfrey Atsa"
    )

    print("Database has been seeded with staff, departments, rooms, reservations, and orders.")

if __name__ == '__main__':
    initialize_database()
