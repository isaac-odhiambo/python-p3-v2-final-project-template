from models.__init__ import CURSOR, CONN

class Room:
    all = {}

    def __init__(self, room_number, room_type, price, id=None):
        self.id = id
        self.room_number = room_number
        self.room_type = room_type
        self.price = price

    def __repr__(self):
        return (f"<Room {self.id}: Room Number: {self.room_number}, " +
                f"Type: {self.room_type}, Price: {self.price}>")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS rooms (
            id INTEGER PRIMARY KEY,
            room_number TEXT,
            room_type TEXT,
            price REAL)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS rooms;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO rooms (room_number, room_type, price)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.room_number, self.room_type, self.price))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE rooms
            SET room_number = ?, room_type = ?, price = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.room_number, self.room_type, self.price, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM rooms
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, room_number, room_type, price):
        room = cls(room_number, room_type, price)
        room.save()
        return room

    @classmethod
    def instance_from_db(cls, row):
        room = cls.all.get(row[0])
        if room:
            room.room_number = row[1]
            room.room_type = row[2]
            room.price = row[3]
        else:
            room = cls(row[1], row[2], row[3])
            room.id = row[0]
            cls.all[room.id] = room
        return room

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM rooms
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM rooms
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
