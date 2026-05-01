class PasswordEntry:
    def __init__(self, website, username, password, category="", notes=""):
        self.website = website
        self.username = username
        self.password = password
        self.category = category
        self.notes = notes

    def __str__(self):
        return f"{self.website} ({self.username})"