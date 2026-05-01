import sqlite3


class Database:
    def __init__(self, db_name="vault.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS password_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            category TEXT,
            notes TEXT
        )
        """)

        self.connection.commit()

    def get_connection(self):
        return self.connection