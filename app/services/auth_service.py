import hashlib


class AuthService:
    def __init__(self, db):
        self.connection = db.get_connection()
        
    # Methode zum Hashen eines Passworts
    def hash_password(self, password: str) -> str:
        # SHA256 erstellt einen Hash-Wert aus dem Passwort
        # encode() wandelt Text in Bytes um
        # hexdigest() gibt den Hash als lesbaren Text zurück
        return hashlib.sha256(password.encode()).hexdigest()

    # Speichert das Master-Passwort in der Datenbank
    def set_master_password(self, password: str):
        cursor = self.connection.cursor()

        # Passwort wird zuerst verschlüsselt
        hashed = self.hash_password(password) 

        # Löscht vorhandenes Master-Passwort, damit nur ein Passwort existiert
        cursor.execute("DELETE FROM master")

        # Speichert den neuen Hash in der Tabelle
        cursor.execute("INSERT INTO master (id, password_hash) VALUES (1, ?)", (hashed,))
        self.connection.commit()

    # Überprüft, ob das eingegebene Passwort korrekt ist
    def verify_password(self, password: str) -> bool:
        cursor = self.connection.cursor()
         # Holt gespeicherten Passwort-Hash aus der Datenbank
        cursor.execute("SELECT password_hash FROM master WHERE id=1")
        # Liest die erste gefundene Zeile
        row = cursor.fetchone()

        # Falls kein Passwort gespeichert wurde
        if not row:
            return False
        
        # Nimmt den Hash aus der Datenbank
        stored_hash = row[0]

        # Vergleicht gespeicherten Hash mit dem Hash des eingegebenen Passworts
        return stored_hash == self.hash_password(password)
    
    # Prüft, ob bereits ein Master-Passwort existiert
    def is_master_set(self) -> bool:
        cursor = self.connection.cursor()
        # Sucht nach einem Eintrag mit id=1
        cursor.execute("SELECT * FROM master WHERE id=1")
        # Gibt True zurück, wenn ein Eintrag existiert
        return cursor.fetchone() is not None