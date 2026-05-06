import random
import string


class PasswordGenerator:

    @staticmethod
    def generate(length=12):
        chars = string.ascii_letters + string.digits + "!@#$%&*"

        return ''.join(random.choice(chars) for _ in range(length))