from app.models.password_entry import PasswordEntry # Importiert das Datenmodell für einen Passwort-Eintrag

class VaultService:
    def __init__(self, repository, crypto_service): # Übergibt Repository und Verschlüsselungs-Service
        self.repository = repository # Speichert Repository für Datenbankzugriffe
        self.crypto_service = crypto_service # Speichert CryptoService für Verschlüsselung

    def add_password(self, website, username, password, category="", notes=""):
        encrypted_password = self.crypto_service.encrypt(password) # Verschlüsselt das Passwort vor dem Speichern
        
        # Erstellt neues PasswordEntry-Objekt
        entry = PasswordEntry(
            website,
            username,
            encrypted_password,
            category,
            notes
        )

        self.repository.add_entry(entry) # Speichert den Eintrag in der Datenbank

    def get_passwords(self): # Holt alle gespeicherten Passwörter
        entries = self.repository.get_all_entries()
        result = [] # Leere Liste für entschlüsselte Daten

        for entry in entries:
            entry_id, website, username, encrypted_password, category, notes = entry # Zerlegt die Daten aus der Datenbank
            decrypted_password = self.crypto_service.decrypt(encrypted_password) # Entschlüsselt das Passwort

            result.append((entry_id, website, username, decrypted_password, category, notes)) # Fügt entschlüsselten Eintrag zur Ergebnisliste hinzu

        return result