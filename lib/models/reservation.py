from models.__init__ import CURSOR, CONN

class Reservation:
    all = {}

    def __init__(self, room_id, guest_name, start_date, end_date, staff_id=None, department_id=None, id=None):
        self.id = id
        self.room_id = room_id
        self.guest_name = guest_name
        self.start_date = start_date
        self.end_date = end_date
        self.staff_id = staff_id
        self.department_id = department_id

    def __repr__(self):
        return (f"<Reservation {self.id}: Room ID: {self.room_id}, Guest Name: {self.guest_name}, "
                f"Start Date: {self.start_date}, End Date: {self.end_date}>")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY,
            room_id INTEGER,
            guest_name TEXT,
            start_date TEXT,
            end_date TEXT,
            staff_id INTEGER,
            department_id INTEGER,
            FOREIGN KEY (room_id) REFERENCES rooms(id),
            FOREIGN KEY (staff_id) REFERENCES staff(id),
            FOREIGN KEY (department_id) REFERENCES departments(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS reservations;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO reservations (room_id, guest_name, start_date, end_date, staff_id, department_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.room_id, self.guest_name, self.start_date, self.end_date, self.staff_id, self.department_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE reservations
            SET room_id = ?, guest_name = ?, start_date = ?, end_date = ?, staff_id = ?, department_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.room_id, self.guest_name, self.start_date, self.end_date, self.staff_id, self.department_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM reservations
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, room_id, guest_name, start_date, end_date, staff_id=None, department_id=None):
        reservation = cls(room_id, guest_name, start_date, end_date, staff_id, department_id)
        reservation.save()
        return reservation

    @classmethod
    def instance_from_db(cls, row):
        reservation = cls.all.get(row[0])
        if reservation:
            reservation.room_id = row[1]
            reservation.guest_name = row[2]
            reservation.start_date = row[3]
            reservation.end_date = row[4]
            reservation.staff_id = row[5]
            reservation.department_id = row[6]
        else:
            reservation = cls(row[1], row[2], row[3], row[4], row[5], row[6])
            reservation.id = row[0]
            cls.all[reservation.id] = reservation
        return reservation

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM reservations
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM reservations
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
