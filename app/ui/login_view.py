import customtkinter as ctk


class LoginView(ctk.CTkFrame):
    def __init__(self, master, on_login):
        super().__init__(master)
        self.on_login = on_login

        self.configure(fg_color="#0F0F12")

        self.card = ctk.CTkFrame(
            self,
            width=360,
            height=320,
            corner_radius=18,
            fg_color="#1A1A1F"
        )
        self.card.place(relx=0.5, rely=0.5, anchor="center")

        self.title = ctk.CTkLabel(
            self.card,
            text="🔐 RedVault",
            font=("Arial", 28, "bold"),
            text_color="white"
        )
        self.title.pack(pady=(35, 10))

        self.subtitle = ctk.CTkLabel(
            self.card,
            text="Tresor mit Master-Passwort entsperren",
            font=("Arial", 14),
            text_color="#B8B8B8"
        )
        self.subtitle.pack(pady=(0, 25))

        self.password_entry = ctk.CTkEntry(
            self.card,
            width=260,
            height=42,
            placeholder_text="Master-Passwort",
            show="*",
            fg_color="#111116",
            border_color="#2A2A32",
            text_color="white"
        )
        self.password_entry.pack(pady=10)

        self.login_button = ctk.CTkButton(
            self.card,
            text="Tresor entsperren",
            width=260,
            height=42,
            fg_color="#C60018",
            hover_color="#990013",
            command=self.login
        )
        self.login_button.pack(pady=15)

        self.message = ctk.CTkLabel(
            self.card,
            text="",
            text_color="#FF4D4D",
            font=("Arial", 12)
        )
        self.message.pack()

        self.password_entry.bind("<Return>", lambda event: self.login())

    def login(self):
        password = self.password_entry.get()

        if not password:
            self.message.configure(text="Bitte Master-Passwort eingeben.")
            return

        self.on_login(password)

    def show_error(self, text):
        self.message.configure(text=text)