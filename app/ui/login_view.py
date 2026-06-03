import customtkinter as ctk

from app.services.crypto_service import hash_master_password, verify_master_password # Funktionen für Passwort-Hashing und Überprüfung



class LoginView(ctk.CTkFrame):
    def __init__(self, master, db, on_login_success):
        super().__init__(master, fg_color="#0b0b0b") # Basis-Frame initialisieren

        self.db = db
        self.conn = db.connection # Datenbankverbindung speichern
        self.on_login_success = on_login_success

        self.setup_master_password() # Erstellt Master-Passwort beim ersten Start
        self.create_widgets()

    def setup_master_password(self):  # Speichert Hash + Salt in der Datenbank
        cursor = self.conn.cursor()

        cursor.execute("SELECT value FROM settings WHERE key='master_hash'")  # Prüft ob Passwort bereits existiert
        result = cursor.fetchone()

        if result is None:
            salt, pw_hash = hash_master_password(MASTER_PASSWORD)# Passwort hashen

            cursor.execute(
                "INSERT INTO settings (key, value) VALUES (?, ?)",
                ("master_salt", salt)
            )

            cursor.execute(
                "INSERT INTO settings (key, value) VALUES (?, ?)",
                ("master_hash", pw_hash)
            )

            self.conn.commit()

    def create_widgets(self):
        title_frame = ctk.CTkFrame(self, fg_color="transparent")
        title_frame.pack(pady=(20, 10))

        ctk.CTkLabel(
            title_frame,
            text="RED",
            font=("Arial", 28, "bold"),
            text_color="#e50914"
        ).pack(side="left")

        ctk.CTkLabel(
            title_frame,
            text="VAULT",
            font=("Arial", 28, "bold"),
            text_color="#E5E5E5"
        ).pack(side="left")

        ctk.CTkLabel(
            self,
            text="Master-Passwort",
            text_color="#E5E5E5"
        ).pack(pady=5)

        # Passwort-Eingabefeld
        self.password_entry = ctk.CTkEntry(
            self,
            show="*",
            width=220,
            height=40,
            fg_color="#1c1c1c",
            text_color="white",
            border_color="#e50914"
        )
        self.password_entry.pack(pady=10)

        self.error_label = ctk.CTkLabel(
            self,
            text="",
            text_color="#e50914"
        )
        self.error_label.pack()

        ctk.CTkButton(
            self,
            text="Entsperren",
            command=self.check_login,
            fg_color="#e50914",
            hover_color="#ff1a25",
            text_color="white",
            width=200,
            height=40
        ).pack(pady=15)

    def check_login(self): # Überprüft eingegebenes Passwort
        password = self.password_entry.get() # Eingegebenes Passwort holen
        cursor = self.conn.cursor()

        cursor.execute("SELECT value FROM settings WHERE key='master_salt'")
        salt = cursor.fetchone()[0]

        cursor.execute("SELECT value FROM settings WHERE key='master_hash'")
        saved_hash = cursor.fetchone()[0]

        if verify_master_password(password, salt, saved_hash): # Öffnet Dashboard bei korrektem Passwort
            self.on_login_success()
        else:
            self.error_label.configure(text="Falsches Passwort")