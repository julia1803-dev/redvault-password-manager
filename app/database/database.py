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

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS master (
            id INTEGER PRIMARY KEY,
            password_hash TEXT NOT NULL
        )
        """)

        self.connection.commit()

    def get_connection(self):
        return self.connection

    def add_entry(self, website, username, password):
        cursor = self.connection.cursor()
        cursor.execute("""
        INSERT INTO password_entries (website, username, password)
        VALUES (?, ?, ?)
        """, (website, username, password))
        self.connection.commit()

    def get_entries(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, website, username, password FROM password_entries")

        rows = cursor.fetchall()
        return rows
    
    def delete_entry(self, entry_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM password_entries WHERE id = ?", (entry_id,))
        self.connection.commit()

    def update_entry(self, entry_id, website, username, password):
        cursor = self.connection.cursor()
        cursor.execute("""
        UPDATE password_entries
        SET website = ?, username = ?, password = ?
        WHERE id = ?
        """, (website, username, password, entry_id))
        self.connection.commit()

        