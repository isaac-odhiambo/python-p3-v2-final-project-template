from models.__init__ import CURSOR, CONN

class Order:
    all = {}

    def __init__(self, room_id, staff_id, guest_name, id=None):
        self.id = id
        self.room_id = room_id
        self.staff_id = staff_id
        self.guest_name = guest_name

    def __repr__(self):
        return (f"<Order {self.id}: Room ID: {self.room_id}, " +
                f"Staff ID: {self.staff_id}, Guest: {self.guest_name}>")

    @property
    def room_id(self):
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        if isinstance(room_id, int):
            # Import inside method to avoid circular dependency
            from models.room import Room
            if Room.find_by_id(room_id):
                self._room_id = room_id
            else:
                raise ValueError("room_id must reference a valid room in the database")
        else:
            raise ValueError("room_id must be an integer")

    @property
    def staff_id(self):
        return self._staff_id

    @staff_id.setter
    def staff_id(self, staff_id):
        if isinstance(staff_id, int):
            # Import inside method to avoid circular dependency
            from models.staff import Staff
            if Staff.find_by_id(staff_id):
                self._staff_id = staff_id
            else:
                raise ValueError("staff_id must reference a valid staff in the database")
        else:
            raise ValueError("staff_id must be an integer")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            room_id INTEGER,
            staff_id INTEGER,
            guest_name TEXT,
            FOREIGN KEY (room_id) REFERENCES rooms(id),
            FOREIGN KEY (staff_id) REFERENCES staff(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS orders;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO orders (room_id, staff_id, guest_name)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.room_id, self.staff_id, self.guest_name))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE orders
            SET room_id = ?, staff_id = ?, guest_name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.room_id, self.staff_id, self.guest_name, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM orders
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, room_id, staff_id, guest_name):
        order = cls(room_id, staff_id, guest_name)
        order.save()
        return order

    @classmethod
    def instance_from_db(cls, row):
        order = cls.all.get(row[0])
        if order:
            order.room_id = row[1]
            order.staff_id = row[2]
            order.guest_name = row[3]
        else:
            order = cls(row[1], row[2], row[3])
            order.id = row[0]
            cls.all[order.id] = order
        return order

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM orders
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM orders
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_guest_name(cls, guest_name):
        sql = """
            SELECT *
            FROM orders
            WHERE guest_name = ?
        """
        row = CURSOR.execute(sql, (guest_name,)).fetchone()
        return cls.instance_from_db(row) if row else None
