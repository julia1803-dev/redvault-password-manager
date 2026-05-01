from app.database.database import Database
from app.database.password_repository import PasswordRepository
from app.services.vault_service import VaultService
from app.services.crypto_service import CryptoService


def main():
    db = Database()
    repo = PasswordRepository(db)
    crypto = CryptoService()

    service = VaultService(repo, crypto)

    service.add_password("github.com", "test@mail.com", "MeinPasswort123")

    entries = service.get_passwords()

    for entry in entries:
        print(entry)


if __name__ == "__main__":
    main()