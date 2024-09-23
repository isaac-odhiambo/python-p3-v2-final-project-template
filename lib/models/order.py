from models.__init__ import CURSOR, CONN

class Order:
    all = {}

    def __init__(self, room_id, quantity, guest_name, total_price=None, id=None):
        self.id = id
        self.room_id = room_id
        self.quantity = quantity
        self.guest_name = guest_name
        self.total_price = total_price

    def __repr__(self):
        return (f"<Order {self.id}: Room {self.room_id}, " +
                f"Quantity {self.quantity}, Guest {self.guest_name}>")

    @classmethod
    def create_table(cls):
        """ Create the orders table """
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY,
                room_id INTEGER,
                quantity INTEGER,
                guest_name TEXT,
                total_price REAL,
                FOREIGN KEY (room_id) REFERENCES rooms(id)
            )
        """)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the orders table """
        CURSOR.execute("DROP TABLE IF EXISTS orders")
        CONN.commit()

    def save(self):
        """ Insert or update order in the database """
        if self.id is None:
            CURSOR.execute("""
                INSERT INTO orders (room_id, quantity, guest_name, total_price)
                VALUES (?, ?, ?, ?)
            """, (self.room_id, self.quantity, self.guest_name, self.total_price))
            self.id = CURSOR.lastrowid
        else:
            CURSOR.execute("""
                UPDATE orders
                SET room_id = ?, quantity = ?, guest_name = ?, total_price = ?
                WHERE id = ?
            """, (self.room_id, self.quantity, self.guest_name, self.total_price, self.id))
        CONN.commit()
    
    def update(self):
        """ Update the order in the database """
        if self.id is not None:  # Ensure the order has an ID before updating
            CURSOR.execute("""
                UPDATE orders
                SET room_id = ?, quantity = ?, guest_name = ?, total_price = ?
                WHERE id = ?
            """, (self.room_id, self.quantity, self.guest_name, self.total_price, self.id))
            CONN.commit()
    


    @classmethod
    def find_by_id(cls, id):
        """ Find an order by its ID """
        row = CURSOR.execute("SELECT * FROM orders WHERE id = ?", (id,)).fetchone()
        if row:
            return cls(row[1], row[2], row[3], row[4], row[0])  # Adjusted to unpack row correctly
        return None

    @classmethod
    def create(cls, room_id, quantity, guest_name, total_price):
        """ Create a new order and save it to the database """
        order = cls(room_id, quantity, guest_name, total_price)
        order.save()
        return order

    @classmethod
    def get_all(cls):
        """ Get all orders from the database """
        rows = CURSOR.execute("SELECT * FROM orders").fetchall()
        return [cls(row[1], row[2], row[3], row[4], row[0]) for row in rows]  # Adjusted to unpack row correctly

    def delete(self):
        """ Delete the order from the database """
        CURSOR.execute("DELETE FROM orders WHERE id = ?", (self.id,))
        CONN.commit()
