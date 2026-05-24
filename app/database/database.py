import sqlite3


class Database:
    # Verbindung zur SQLite-Datenbank
    def __init__(self, db_name="vault.db"):
        try:
            self.connection = sqlite3.connect(db_name)
            self.create_tables()
        except sqlite3.Error as e:
            print("Fehler beim Verbinden mit der Datenbank:", e)
            
    # Erstellung Tabellen
    def create_tables(self):
        try:
            cursor = self.connection.cursor() # Cursor wird benötigt um SQL-Befehle auszuführen

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
            # Tabelle für Einstellungen erstellen
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value BLOB NOT NULL
            )
            """)

            self.connection.commit()

        except sqlite3.Error as e:
            print("Fehler beim Erstellen der Tabellen:", e)

    # Gibt die aktuelle Datenbankverbindung zurück
    def get_connection(self):
        return self.connection

    def add_entry(self, website, username, password, category=None, notes=None):
        try:
            cursor = self.connection.cursor()
             # Neuer Datensatz wird in die Tabelle eingefügt
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
            # Alle Daten aus password_entries auswählen
            cursor.execute("""
            SELECT id, website, username, password, category, notes
            FROM password_entries
            """)
            # Alle Ergebnisse zurückgeben
            return cursor.fetchall()

        except sqlite3.Error as e:
            print("Fehler beim Laden der Einträge:", e)
            return [] #Beim Fehler gibt eine leere Liste zurück

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
            # Vorhandene Daten aktualisieren
            cursor.execute("""
            UPDATE password_entries
            SET website = ?, username = ?, password = ?, category = ?, notes = ?
            WHERE id = ?
            """, (website, username, password, category, notes, entry_id))

            self.connection.commit()

        except sqlite3.Error as e:
            print("Fehler beim Aktualisieren:", e)
    # Schliesst die Verbindung zur Datenbank
    def close(self):
        try:
            self.connection.close()
        except sqlite3.Error as e:
            print("Fehler beim Schließen der Verbindung:", e)

        # Speichert Einstellungen wie Salt oder Passwort-Hash in der Tabelle settings
    def save_setting(self, key, value):
        cursor = self.connection.cursor()

        cursor.execute("""
        INSERT OR REPLACE INTO settings (key, value)
        VALUES (?, ?)
        """, (key, value))

        self.connection.commit()


    # Holt gespeicherte Einstellungen
    def get_setting(self, key):
        cursor = self.connection.cursor()

        cursor.execute("""
        SELECT value FROM settings
        WHERE key = ?
        """, (key,))

        row = cursor.fetchone()

        return row[0] if row else None