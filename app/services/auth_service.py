from app.services.crypto_service import (
        hash_master_password,
        verify_master_password
    )


class AuthService:
    def __init__(self, db):
        self.connection = db.get_connection()

    # Speichert das Master-Passwort in der Datenbank
    def set_master_password(self, password: str):
        cursor = self.connection.cursor()

        # Passwort wird zuerst gehasht
        # Zusätzlich wird ein zufälliger Salt erstellt
        salt, password_hash = hash_master_password(password) 

        self.connection.execute("DELETE FROM settings") # Alte Sicherheitswerte löschen, damit nur ein Master-Passwort existiert

        cursor = self.connection.cursor()

        cursor.execute("""
        INSERT INTO settings (key, value)
        VALUES (?, ?)
        """, ("master_salt", salt))  # Speichert den Salt in der Tabelle settings

        cursor.execute("""
        INSERT INTO settings (key, value)
        VALUES (?, ?)
        """, ("master_hash", password_hash)) # Speichert den Passwort-Hash

        self.connection.commit()

    # Überprüft, ob das eingegebene Passwort korrekt ist
    def verify_password(self, password: str) -> bool:
        cursor = self.connection.cursor()
         # Holt Salt aus der Tabelle settings
        cursor.execute("""
        SELECT value FROM settings
        WHERE key='master_salt'
        """) # Holt den gespeicherten Salt aus der Datenbank

        salt_row = cursor.fetchone()

        # Holt gespeicherten Hash
        cursor.execute("""
        SELECT value FROM settings
        WHERE key='master_hash'
        """)

        hash_row = cursor.fetchone()

        # Falls Salt oder Hash fehlen
        if not salt_row or not hash_row:
            return False

        # Werte auslesen
        salt = salt_row[0]
        saved_hash = hash_row[0]

        # Passwort prüfen
        return verify_master_password(password, salt, saved_hash) # Dazu wird ein neuer Hash erzeugt und mit dem gespeicherten Hash verglichen
    
    # Prüft, ob bereits ein Master-Passwort existiert
    def is_master_set(self) -> bool:
        cursor = self.connection.cursor()
        # Prüft, ob ein Master-Hash in settings existiert
        cursor.execute("""
        SELECT * FROM settings WHERE key='master_hash' """)
        # Gibt True zurück, wenn ein Eintrag existiert
        return cursor.fetchone() is not None