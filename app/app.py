import customtkinter as ctk

from app.database.database import Database
from app.database.password_repository import PasswordRepository
from app.services.vault_service import VaultService
from app.services.crypto_service import CryptoService
from app.services.auth_service import AuthService

from app.ui.login_view import LoginView
from app.ui.dashboard_view import DashboardView


class RedVaultApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("RedVault Password Manager")
        self.geometry("900x600")
        self.minsize(800, 500)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.db = Database()
        self.auth_service = AuthService(self.db)

        self.repo = PasswordRepository(self.db)
        self.crypto = CryptoService()
        self.vault_service = VaultService(self.repo, self.crypto)

        self.login_view = LoginView(self, self.handle_login)
        self.login_view.pack(fill="both", expand=True)

    def handle_login(self, password):
        if not self.auth_service.is_master_set():
            self.auth_service.set_master_password(password)
            self.show_dashboard()
            return

        if self.auth_service.verify_password(password):
            self.show_dashboard()
        else:
            self.login_view.show_error("Falsches Master-Passwort.")

    def show_dashboard(self):
        self.login_view.destroy()

        dashboard = DashboardView(self, self.vault_service)
        dashboard.pack(fill="both", expand=True)