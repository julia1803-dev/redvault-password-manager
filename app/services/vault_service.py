from app.models.password_entry import PasswordEntry


class VaultService:
    def __init__(self, repository):
        self.repository = repository

    def add_password(self, website, username, password, category="", notes=""):
        entry = PasswordEntry(website, username, password, category, notes)
        self.repository.add_entry(entry)

    def get_passwords(self):
        return self.repository.get_all_entries()