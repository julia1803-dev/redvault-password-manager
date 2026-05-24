# das Speichern in der Datenbank.
# Importiert das Datenmodell PasswordEntry
from app.models.password_entry import PasswordEntry 

# Das Modell repräsentiert einen Passwort-Eintrag als Objekt
class PasswordRepository:

    # Holt die Datenbankverbindung aus der Database-Klasse
    def __init__(self, db):
        self.connection = db.get_connection()

    def add_entry(self, entry: PasswordEntry):
        cursor = self.connection.cursor()
        # SQL INSERT-Befehl zum Speichern eines neuen Eintrags
        cursor.execute("""
            INSERT INTO password_entries (website, username, password, category, notes)
            VALUES (?, ?, ?, ?, ?)
        """, (entry.website, entry.username, entry.password, entry.category, entry.notes)) # Fügt einen neuen Datensatz in die Tabelle ein
        self.connection.commit()

    # Lädt alle gespeicherten Einträge aus der Datenbank
    def get_all_entries(self):
        cursor = self.connection.cursor()
        # Alle Datensätze aus der Tabelle auswählen
        cursor.execute("SELECT * FROM password_entries")

        # Ergebnisse zurückgeben
        return cursor.fetchall()