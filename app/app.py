import customtkinter as ctk

from app.database.database import Database
from app.ui.login_view import LoginView # Login-Oberfläche importieren
from app.ui.dashboard_view import DashboardView


class RedVaultApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("RedVault") # Fenstertitel setzen
        self.geometry("1000x650")
        self.configure(fg_color="#0b0b0b")# Hintergrundfarbe setzen

        ctk.set_appearance_mode("dark") # Dark Mode aktivieren
        ctk.set_default_color_theme("dark-blue")

        self.db = Database()
        self.show_login() #Beim Start wird zuerst das Login-Fenster angezeigt

    def clear_window(self):# Diese Methode löscht alle aktuellen Elemente im Fenster
        for widget in self.winfo_children():
            widget.destroy()

    def show_login(self): #Diese Methode zeigt das Login-Fenster
        self.clear_window()
        LoginView(self, self.db, self.show_dashboard).pack(fill="both", expand=True)

    def show_dashboard(self):# Öffnet das Dashboard nach erfolgreichem Login
        self.clear_window()
        DashboardView(self, self.db).pack(fill="both", expand=True)