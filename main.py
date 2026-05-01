from app.database.database import Database
from app.database.password_repository import PasswordRepository
from app.services.vault_service import VaultService


def main():
    db = Database()
    repo = PasswordRepository(db)
    service = VaultService(repo)

    # Test: Passwort speichern
    service.add_password("github.com", "user@test.com", "123456")

    # Test: Anzeigen
    entries = service.get_passwords()
    for entry in entries:
        print(entry)


if __name__ == "__main__":
    main()