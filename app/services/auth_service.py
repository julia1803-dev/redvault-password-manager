import hashlib


class AuthService:
    def __init__(self, db):
        self.connection = db.get_connection()

    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def set_master_password(self, password: str):
        cursor = self.connection.cursor()
        hashed = self.hash_password(password)

        cursor.execute("DELETE FROM master")
        cursor.execute("INSERT INTO master (id, password_hash) VALUES (1, ?)", (hashed,))
        self.connection.commit()

    def verify_password(self, password: str) -> bool:
        cursor = self.connection.cursor()
        cursor.execute("SELECT password_hash FROM master WHERE id=1")
        row = cursor.fetchone()

        if not row:
            return False

        stored_hash = row[0]
        return stored_hash == self.hash_password(password)

    def is_master_set(self) -> bool:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM master WHERE id=1")
        return cursor.fetchone() is not None