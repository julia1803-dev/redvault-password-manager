import sqlite3

# Die Klasse Database kapselt alle Datenbank-Funktionen
class Database:
    # Konstruktor: Wird automatisch aufgerufen, wenn ein Objekt erstellt wird
    def __init__(self, db_name="vault.db"):
        # Verbindung zur SQLite-Datenbank herstellen
        # Falls die Datei nicht existiert, wird sie automatisch erstellt
        try:
            self.connection = sqlite3.connect(db_name)
            self.create_tables()
        except sqlite3.Error as e:
            print("Fehler beim Verbinden mit der Datenbank:", e)


    # Methode zum Erstellen der notwendigen Tabellen
    def create_tables(self):
        try:
            cursor = self.connection.cursor()
            # Cursor-Objekt erstellen → damit können SQL-Befehle ausgeführt werden
            # Tabelle für Passwort-Einträge erstellen
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS password_entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT, -- eindeutige ID (automatisch hochzählend)
                website TEXT NOT NULL, -- Name der Website
                username TEXT NOT NULL, -- Benutzername
                password TEXT NOT NULL,  -- Passwort
                category TEXT,  -- optionale Kategorie
                notes TEXT -- optionale Notizen
            )
            """)
            # Tabelle für das Master-Passwort erstellen
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS master (
                id INTEGER PRIMARY KEY, -- nur ein Eintrag erwartet
                password_hash TEXT NOT NULL -- gespeicherter Hash des Master-Passworts
            )
            """)
            # Änderungen speichern
            self.connection.commit()
        except sqlite3.Error as e:
            print("Fehler beim Erstellen der Tabellen:", e)


    # Gibt die aktuelle Datenbankverbindung zurück
    def get_connection(self):
        return self.connection
    
    # Fügt einen neuen Passwort-Eintrag hinzu
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

     # Holt alle gespeicherten Einträge aus der Datenbank
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
        
    # Löscht einen Eintrag anhand seiner ID
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
    # Verbindung sauber schließen
    def close(self):
        try:
            self.connection.close()
        except sqlite3.Error as e:
            print("Fehler beim Schließen der Verbindung:", e)


        