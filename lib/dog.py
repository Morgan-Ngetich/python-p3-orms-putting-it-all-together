import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:
    def __init__(self, name="joey", breed="cocker spaniel"):
        self.id = None
        self.name = name
        self.breed = breed
    
    @classmethod
    def create_table(cls):
        sql = 
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS dogs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                breed TEXT
            )
        """)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute("DROP TABLE IF EXISTS dogs")
        CONN.commit()

    def save(self):
        CURSOR.execute('''
            INSERT INTO dogs (name, breed)
            VALUES (?, ?)
        ''', (self.name, self.breed))
        self.id = CURSOR.lastrowid
        CONN.commit()

    def update(self):
        CURSOR.execute('''
            UPDATE dogs
            SET name = ?
            WHERE id = ?
        ''', (self.name, self.id))
        CONN.commit()

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute('''
            SELECT * FROM dogs
            WHERE id = ?
        ''', (id,))
        row = CURSOR.fetchone()
        if row:
            return cls(*row[1:])
        return None

    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute('''
            SELECT * FROM dogs
            WHERE name = ?
        ''', (name,))
        row = CURSOR.fetchone()
        if row:
            return cls(*row[1:])
        return None

    @classmethod
    def get_all(cls):
        CURSOR.execute('SELECT * FROM dogs')
        rows = CURSOR.fetchall()
        dogs = []
        for row in rows:
            dogs.append(cls(*row[1:]))
        return dogs

    @classmethod
    def create(cls, name, breed):
        dog = cls(name, breed)
        dog.save()
        return dog
