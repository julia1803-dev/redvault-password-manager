class PasswordEntry:
    #Psswort-Eintrag
    def __init__(self, website, username, password, category="", notes=""):
        self.website = website
        self.username = username
        self.password = password
        self.category = category
        self.notes = notes
        self.password_entry.bind("<KeyRelease>", self.update_strength)# Passwort-Eingabe überwachen. Reagiert auf jede Tasteneingabe. 
        #Die Passwort-Stärke live aktualisiert wird, während der Benutzer tippt

    def __str__(self):
        return f"{self.website} ({self.username})" # Definiert die Text-Ausgabe des Objekts