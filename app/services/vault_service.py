from app.models.password_entry import PasswordEntry


class VaultService:
    def __init__(self, repository, crypto_service):
        self.repository = repository
        self.crypto_service = crypto_service

    def add_password(self, website, username, password, category="", notes=""):
        encrypted_password = self.crypto_service.encrypt(password)

        entry = PasswordEntry(
            website,
            username,
            encrypted_password,
            category,
            notes
        )

        self.repository.add_entry(entry)

    def get_passwords(self):
        entries = self.repository.get_all_entries()
        result = []

        for entry in entries:
            entry_id, website, username, encrypted_password, category, notes = entry
            decrypted_password = self.crypto_service.decrypt(encrypted_password)

            result.append((entry_id, website, username, decrypted_password, category, notes))

        return result