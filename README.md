# Phase 3 CLI+ORM Project Template

## Learning Goals

- Discuss the basic directory structure of a CLI.
- Outline the first steps in building a CLI.

---

## Introduction

You now have a basic idea of what constitutes a CLI. Fork and clone this lesson
for a project template for your CLI.

Take a look at the directory structure:

hotel_management_system/
│
├── models/
│   ├── __init__.py
│   ├── department.py
│   ├── staff.py
│   ├── room.py
│   ├── reservation.py
│   └── order.py
│
├── helpers/
│   ├── __init__.py
│   ├── department_helpers.py
│   ├── staff_helpers.py
│   ├── room_helpers.py
│   ├── reservation_helpers.py
│   └── order_helpers.py
│
├── cli.py
├── config.py
├── requirements.txt
└── README.md

# Relationship 
Department and Staff
One-to-Many Relationship: A department can have many staff members, but each staff member belongs to only one department.

Department: Represents the organizational unit within the hotel (e.g., Housekeeping, Front Desk).
Staff: Represents individual employees who work in a specific department.
Key Attributes:

Department: id, name, location
Staff: id, name, job_title, department_id
Relationship:

Each Staff record has a department_id that links it to a Department.
You can find all staff in a department using the find_by_department_id(department_id) function in the Staff model.
2. Room and Reservation
One-to-Many Relationship: A room can be reserved many times (in different periods), but each reservation is for only one room.

Room: Represents the individual rooms available in the hotel.
Reservation: Represents a booking made for a specific room.
Key Attributes:

Room: id, number, room_type, price
Reservation: id, room_id, guest_name, start_date, end_date, staff_id, department_id
Relationship:

Each Reservation record has a room_id that links it to a Room.
You can find all reservations for a specific room using the find_by_room_id(room_id) function (if implemented in the Reservation model).
3. Room and Order
One-to-Many Relationship: A room can have many orders placed against it, but each order is associated with only one room.

Room: Represents the individual rooms available in the hotel.
Order: Represents a food or service order placed by a guest in a specific room.
Key Attributes:

Room: id, number, room_type, price
Order: id, room_id, item, quantity, total_price, staff_id, department_id
Relationship:

Each Order record has a room_id that links it to a Room.
You can find all orders for a specific room using the find_by_room_id(room_id) function (if implemented in the Order model).
4. Reservation and Staff
Many-to-One Relationship: Many reservations can be handled by a single staff member.

Reservation: Represents a booking that can involve a staff member (e.g., handling the reservation).
Staff: Represents the staff member who managed or is associated with the reservation.
Key Attributes:

Reservation: id, staff_id
Staff: id, name, job_title
Relationship:

Each Reservation record has a staff_id that links it to a Staff member.
You can find all reservations handled by a specific staff member using the find_by_staff_id(staff_id) function (if implemented in the Reservation model).
5. Reservation and Department
Many-to-One Relationship: Many reservations can be associated with a single department.

Reservation: Represents a booking that can be associated with a department (e.g., for departmental tracking).
Department: Represents the department that is associated with the reservation.
Key Attributes:

Reservation: id, department_id
Department: id, name, location
Relationship:

Each Reservation record has a department_id that links it to a Department.
You can find all reservations associated with a specific department using the find_by_department_id(department_id) function (if implemented in the Reservation model).


# Staff Model
get_all(): Retrieves all staff records from the database.
find_by_name(name): Searches for a staff member by their name and returns it if found.
find_by_id(id_): Searches for a staff member by their unique ID and returns it if found.
create(name, job_title, department_id): Creates a new staff member with the specified name, job title, and department ID.
update(): Updates the staff member’s details (name, job title, department ID) in the database.
delete(): Deletes the staff member from the database.
find_by_department_id(department_id): Finds all staff members associated with a specific department ID.

# Room Model
get_all(): Retrieves all room records from the database.
find_by_number(number): Searches for a room by its number and returns it if found.
create(number, room_type, price): Creates a new room with the specified number, room type, and price.
update(): Updates the room’s details (type, price) in the database.
delete(): Deletes the room from the database.

# Reservation Model
get_all(): Retrieves all reservation records from the database.
find_by_id(id_): Searches for a reservation by its unique ID and returns it if found.
create(room_id, guest_name, start_date, end_date, staff_id, department_id): Creates a new reservation with the specified room ID, guest name, start and end dates, staff ID, and department ID.
update(): Updates the reservation details (room ID, guest name, start and end dates, staff ID, department ID) in the database.
delete(): Deletes the reservation from the database.

# Order Model
get_all(): Retrieves all order records from the database.
find_by_id(id_): Searches for an order by its unique ID and returns it if found.
create(room_id, item, quantity, total_price, staff_id, department_id): Creates a new order with the specified room ID, item, quantity, total price, staff ID, and department ID.
update(): Updates the order’s details (room ID, item, quantity, total price, staff ID, department ID) in the database.
delete(): Deletes the order from the database.



# helpers Directory
The helpers directory contains various modules that provide functions to perform specific operations related to different models in your system. Each helper file is designed to handle operations for a particular model, encapsulating logic related to creating, reading, updating, and deleting records, as well as any other domain-specific tasks. This modular approach keeps your code organized and makes it easier to manage and maintain.

Key Functions in helpers Directory:
# department_helpers.py:

list_departments(): Retrieves and prints all departments from the database.
find_department_by_name(name): Searches for a department by its name and prints it. If not found, it provides a message indicating that the department was not found.
find_department_by_id(id_): Finds and prints a department by its ID.
create_department(): Prompts the user to input details and creates a new department in the database.
update_department(id_): Finds a department by its ID, prompts for new details, and updates the department.
delete_department(id_): Finds a department by its ID and deletes it from the database.
list_department_employees(department_id): Lists all employees in a specified department.
staff_helpers.py:

list_staff(): Retrieves and prints all staff members from the database.
find_staff_by_name(name): Searches for a staff member by name and prints their details. If not found, it provides a message indicating that the staff member was not found.
find_staff_by_id(id_): Finds and prints a staff member by their ID.
create_staff(): Prompts the user to input details and creates a new staff member in the database.
update_staff(id_): Finds a staff member by ID, prompts for new details, and updates the staff member.
delete_staff(id_): Finds a staff member by ID and deletes them from the database.
room_helpers.py:

list_rooms(): Retrieves and prints all rooms from the database.
find_room_by_number(number): Searches for a room by its number and prints it. If not found, it provides a message indicating that the room was not found.
create_room(): Prompts the user to input details and creates a new room in the database.
update_room(number): Finds a room by its number, prompts for new details, and updates the room.
delete_room(number): Finds a room by its number and deletes it from the database.
reservation_helpers.py:

list_reservations(): Retrieves and prints all reservations from the database.
find_reservation_by_id(id_): Finds and prints a reservation by its ID.
create_reservation(): Prompts the user to input details and creates a new reservation in the database.
update_reservation(id_): Finds a reservation by ID, prompts for new details, and updates the reservation.
delete_reservation(id_): Finds a reservation by ID and deletes it from the database.
order_helpers.py:

list_orders(): Retrieves and prints all orders from the database.
find_order_by_id(id_): Finds and prints an order by its ID.
create_order(): Prompts the user to input details and creates a new order in the database.
update_order(id_): Finds an order by ID, prompts for new details, and updates the order.
delete_order(id_): Finds an order by ID and deletes it from the database.

## cli.py
The cli.py file is the main entry point for your application. It provides a command-line interface (CLI) that allows users to interact with the system by executing various commands. The CLI will present a menu of options, accept user input, and call the appropriate functions from the helpers modules based on that input.

Key Components of cli.py:
main() Function:

This function is the core of the CLI. It displays the menu repeatedly and processes user input to perform different actions.
It calls the menu() function to display the options and then uses input() to get the user's choice.
Based on the user's choice, it calls the relevant functions from the helpers modules (e.g., list_departments(), create_department(), etc.).
It handles user interactions and maintains the flow of the application, such as exiting the program or performing CRUD operations.
menu() Function:

Displays the available options to the user.
This function is responsible for showing what actions can be performed, such as listing departments, creating a department, etc.
The menu helps users understand what commands are available and how to interact with the application.
Conditional __name__ == "__main__":

Ensures that main() is called only when cli.py is run directly, not when it is imported as a module.
This allows cli.py to function as both a standalone script and a module that can be imported elsewhere if needed.


## Setting Up the Python Environment
# a. Create a Virtual Environment:

Use a virtual environment to manage dependencies and isolate your project

# b. Install Dependencies:

Install necessary packages such as SQLAlchemy for ORM and Alembic for migrations.

Setting Up SQLAlchemy and Alembic
a. Configure SQLAlchemy:

2. Create a config.py file or similar to store database configuration settings.
python

DATABASE_URL = 'sqlite:///example.db'  # or your preferred database URL

# Define Models:
Ensure each model class (Department, Staff, Room, Reservation, Order) is defined with SQLAlchemy ORM mappings.

# Create and Apply Migrations:

Initialize Alembic for migrations.

alembic init alembic
Configure alembic.ini and env.py in the alembic folder to use your database URL and model definitions.
Create initial migration files and apply them.

# 3. Implementing the Helper Functions
a. Define Helper Functions:

Write functions for CRUD operations and other tasks in the helpers module
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head

4. Setting Up CLI
a. Implement CLI Commands:

Ensure cli.py imports the correct functions from helpers and implements a menu system to interact with users.
# Handle User Input and Permissions:

Implement logic to check user roles and permissions before executing commands

2. Credentials
A dictionary named credentials is defined to hold dummy passwords for different user roles (Manager and Staff). This is used for user authentication. 

#### Note the dummy  password in our case is 1234

3. Main Function
The main() function serves as the entry point of the application. It performs the following tasks:

User Authentication: Calls the authenticate_user() function to determine the user's role (Manager, Staff, or Guest).
Menu Display: Enters a loop that continuously displays a menu based on the user’s role and processes their choice until they decide to exit.
4. User Authentication
The authenticate_user() function prompts the user to enter their role and, if applicable, their password:

If the role is either Manager or Staff, it checks the password against the credentials dictionary.
If the password is incorrect, it defaults the user to the Guest role.
If an invalid role is entered, it also defaults to Guest.
5. Menu Display
The menu(role) function prints available options based on the user's role:

Managers have access to all functions (e.g., create, update, delete).
Staff have limited access, mainly to view functions.
Guests can book rooms and view room lists.
6. Choice Handling
The handle_manager_choices(), handle_staff_choices(), and handle_guest_choices() functions process the user's menu choices:

Each function checks the user’s choice and calls the appropriate helper function to execute the selected operation.
If the choice is invalid, an error message is printed.
7. Program Flow
Start the program: The script runs main(), starting the authentication process.
Display menu: Based on the authenticated role, the user is shown relevant options.
User makes a choice: Depending on the user's input, corresponding functions are called to manage departments, staff, rooms, reservations, and orders.
Exit the program: If the user selects option "0", the program calls exit_program() to terminate.


## IMPORTANT NOTEin this project  to access function of manager and staff in CLI use passowrd of 
1234


# Author:
Isaac Odiwuor Odhiambo- student at moringa school 


