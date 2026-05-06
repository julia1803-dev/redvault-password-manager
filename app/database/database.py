import sqlite3


class Database:
    def __init__(self, db_name="vault.db"):
        try:
            self.connection = sqlite3.connect(db_name)
            self.create_tables()
        except sqlite3.Error as e:
            print("Fehler beim Verbinden mit der Datenbank:", e)

    def create_tables(self):
        try:
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
            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value BLOB NOT NULL
            )
            """)

            self.connection.commit()

        except sqlite3.Error as e:
            print("Fehler beim Erstellen der Tabellen:", e)

    def get_connection(self):
        return self.connection

    def add_entry(self, website, username, password, category=None, notes=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            INSERT INTO password_entries (website, username, password, category, notes)
            VALUES (?, ?, ?, ?, ?)
            """, (website, username, password, category, notes))

            self.connection.commit()

        except sqlite3.Error as e:
            print("Fehler beim Hinzufügen eines Eintrags:", e)

    def get_entries(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            SELECT id, website, username, password, category, notes
            FROM password_entries
            """)

            return cursor.fetchall()

        except sqlite3.Error as e:
            print("Fehler beim Laden der Einträge:", e)
            return []

    def delete_entry(self, entry_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM password_entries WHERE id = ?", (entry_id,))
            self.connection.commit()

        except sqlite3.Error as e:
            print("Fehler beim Löschen:", e)

    def update_entry(self, entry_id, website, username, password, category=None, notes=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            UPDATE password_entries
            SET website = ?, username = ?, password = ?, category = ?, notes = ?
            WHERE id = ?
            """, (website, username, password, category, notes, entry_id))

            self.connection.commit()

        except sqlite3.Error as e:
            print("Fehler beim Aktualisieren:", e)

    def close(self):
        try:
            self.connection.close()
        except sqlite3.Error as e:
            print("Fehler beim Schließen der Verbindung:", e)