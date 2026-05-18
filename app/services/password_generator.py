import random
import string


class PasswordGenerator:

    def generate(length=12):
        chars = string.ascii_letters + string.digits + "!@#$%&*"

        return ''.join(random.choice(chars) for _ in range(length)) # join() verbindet alle Zeichen zu einem Text

    # Statische Methode
    # Kann ohne Objekt verwendet werden
    @staticmethod

    
    def check_password_strength(password):
        score = 0

        if len(password) >= 8:
            score += 1

        if any(char.isdigit() for char in password):
            score += 1

        if any(char.isupper() for char in password):
            score += 1

        if any(char in "!@#$%^&*()" for char in password):
            score += 1

        if score <= 1:
            return "Schwach"

        elif score <= 3:
            return "Mittel"

        else:
            return "Stark"