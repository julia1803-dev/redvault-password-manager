import customtkinter as ctk


class DashboardView(ctk.CTkFrame):
    def __init__(self, master, vault_service):
        super().__init__(master)

        self.vault_service = vault_service

        self.configure(fg_color="#0F0F12")

        title = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Arial", 28, "bold"),
            text_color="white"
        )
        title.pack(pady=20)

        self.entries_frame = ctk.CTkFrame(self, fg_color="#1A1A1F")
        self.entries_frame.pack(fill="both", expand=True, padx=40, pady=20)

        self.load_entries()

    def load_entries(self):
        entries = self.vault_service.get_passwords()

        for entry in entries:
            entry_id, website, username, password, category, notes = entry

            text = f"{website} | {username} | {password}"

            label = ctk.CTkLabel(
                self.entries_frame,
                text=text,
                anchor="w",
                text_color="white"
            )
            label.pack(fill="x", padx=10, pady=5)