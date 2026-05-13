import random
import string


class PasswordGenerator:

    # Statische Methode
    # Kann ohne Objekt verwendet werden
    @staticmethod
    def generate(length=12):
        # Erstellt alle erlaubten Zeichen für das Passwort
        chars = string.ascii_letters + string.digits + "!@#$%&*"

        return ''.join(random.choice(chars) for _ in range(length)) # join() verbindet alle Zeichen zu einem Text