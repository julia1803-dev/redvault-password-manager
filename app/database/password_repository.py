from app.models.password_entry import PasswordEntry


class PasswordRepository:
    def __init__(self, db):
        self.connection = db.get_connection()

    def add_entry(self, entry: PasswordEntry):
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO password_entries (website, username, password, category, notes)
            VALUES (?, ?, ?, ?, ?)
        """, (entry.website, entry.username, entry.password, entry.category, entry.notes))
        self.connection.commit()

    def get_all_entries(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM password_entries")
        return cursor.fetchall()