import random
import string


class PasswordGenerator:

    @staticmethod
    def generate(length=12):
        # Mindestens 1 Zeichen jeder Kategorie
        password = [
            random.choice(string.ascii_uppercase),  # Grossbuchstabe
            random.choice(string.ascii_lowercase),  # Kleinbuchstabe
            random.choice(string.digits),           # Zahl
            random.choice("!@#$%^&*()")             # Sonderzeichen
        ]

        # Alle erlaubten Zeichen
        chars = (
            string.ascii_letters +
            string.digits +
            "!@#$%^&*()"
        )

        # Restliche Zeichen zufällig ergänzen
        password += [
            random.choice(chars)
            for _ in range(length - 4)
        ]

        # Zeichen mischen
        random.shuffle(password)

        return ''.join(password)

    @staticmethod
    def check_password_strength(password):
        score = 0

        if len(password) >= 8:
            score += 1

        if any(char.isdigit() for char in password):
            score += 1

        if any(char.isupper() for char in password):
            score += 1

        if any(char.islower() for char in password):
            score += 1

        if any(char in "!@#$%^&*()" for char in password):
            score += 1

        if score <= 2:
            return "Schwach"
        elif score <= 4:
            return "Mittel"
        else:
            return "Stark"