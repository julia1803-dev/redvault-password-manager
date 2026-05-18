import customtkinter as ctk
from PIL import Image
from tkinter import messagebox # Popup-Meldungen

from app.services.password_generator import PasswordGenerator # Passwortgenerator importieren


class DashboardView(ctk.CTkFrame):
    def __init__(self, master, db):
        super().__init__(master, fg_color="#0b0b0b") # Basis-Frame initialisieren

        self.master = master
        self.db = db
        self.passwords_visible = False # Status für Passwortanzeige


        self.create_widgets()
        self.refresh_entries() # Gespeicherte Einträge laden

    def create_widgets(self): #Erstellung komplette Benutzerobefläche
        self.master.title("RedVault Passwortmanager")
        self.master.geometry("1000x650")

        logo_image = ctk.CTkImage(
            light_image=Image.open("assets/logo.png"),
            dark_image=Image.open("assets/logo.png"),
            size=(40, 40)
        )
        self.logo_image = logo_image

        title_frame = ctk.CTkFrame(self, fg_color="transparent")
        title_frame.pack(pady=25)

        ctk.CTkLabel(title_frame, image=logo_image, text="").pack(side="left", padx=(0, 8))

        ctk.CTkLabel(
            title_frame,
            text="RED",
            font=("Arial", 42, "bold"),
            text_color="#e50914"
        ).pack(side="left")

        ctk.CTkLabel(
            title_frame,
            text="VAULT",
            font=("Arial", 42, "bold"),
            text_color="#E5E5E5"
        ).pack(side="left")

        button_frame = ctk.CTkFrame(self, fg_color="transparent") # Bereich für Buttons
        button_frame.pack(pady=10)

        ctk.CTkButton(
            button_frame,
            text="+ Neuer Eintrag",
            command=self.open_new_entry_form,# Öffnet Formular für neuen Eintrag
            fg_color="#e50914",
            hover_color="#ff1a25",
            width=200,
            height=45
        ).grid(row=0, column=0, padx=10)

        self.show_button = ctk.CTkButton(
            button_frame,
            text="Passwörter anzeigen",
            command=self.toggle_passwords,# Zeigt oder versteckt Passwörter
            fg_color="#222222",
            hover_color="#333333",
            width=200,
            height=45
        )
        self.show_button.grid(row=0, column=1, padx=10)

        container = ctk.CTkFrame(self, fg_color="#e50914", corner_radius=16)
        container.pack(padx=40, pady=30, fill="both", expand=True)

        inner = ctk.CTkFrame(container, fg_color="#101010", corner_radius=14)
        inner.pack(padx=2, pady=2, fill="both", expand=True)

        header = ctk.CTkFrame(inner, fg_color="#101010")
        header.pack(fill="x", padx=25, pady=(10, 5))

        header.grid_columnconfigure(0, weight=2)
        header.grid_columnconfigure(1, weight=2)
        header.grid_columnconfigure(2, weight=1)
        header.grid_columnconfigure(3, weight=1)
        header.grid_columnconfigure(4, weight=1)
        header.grid_columnconfigure(5, weight=0)

        ctk.CTkLabel(header, text="Website", text_color="#e50914", width=260, anchor="w").grid(row=0, column=0, padx=10, sticky="w")
        ctk.CTkLabel(header, text="Benutzername", text_color="#e50914", width=270, anchor="w").grid(row=0, column=1, padx=10, sticky="w")
        ctk.CTkLabel(header, text="Passwort", text_color="#e50914", width=160, anchor="w").grid(row=0, column=2, padx=5, sticky="w")
        ctk.CTkLabel(header, text="Kategorie", text_color="#e50914", width=130, anchor="w").grid(row=0, column=3, padx=5, sticky="w")
        ctk.CTkLabel(header, text="Notizen", text_color="#e50914", width=160, anchor="w").grid(row=0, column=4, padx=5, sticky="w")
        ctk.CTkLabel(header, text="Aktionen", text_color="#e50914", width=190, anchor="w").grid(row=0, column=5, padx=(0, 10), sticky="e")

        self.entries_frame = ctk.CTkScrollableFrame(inner, fg_color="#101010") # Scrollbarer Bereich für Passwort-Einträge
        self.entries_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.search_entry = ctk.CTkEntry(self, placeholder_text="Suchen...", width=300)
        self.search_entry.pack(pady=10)
        self.search_entry.bind("<KeyRelease>", lambda event: self.refresh_entries())# Aktualisiert Suche bei jeder Tasteneingabe

    def refresh_entries(self):# Lädt und zeigt alle Einträge neu an
        for widget in self.entries_frame.winfo_children():
            widget.destroy()

        search_text = self.search_entry.get().lower()
        entries = self.db.get_entries()# Holt alle Einträge aus der Datenbank

        for entry in entries:
            entry_id = entry[0]
            website = entry[1]
            username = entry[2]
            password = entry[3]
            category = entry[4]
            notes = entry[5]

            website_filter = website.lower()
            username_filter = username.lower()
            category_filter = (category or "").lower()
            notes_filter = (notes or "").lower()

            if (
                search_text not in website_filter
                and search_text not in username_filter
                and search_text not in category_filter
                and search_text not in notes_filter
            ):
                continue

            shown_password = password if self.passwords_visible else "••••••••"# Passwort sichtbar oder versteckt anzeigen

            row = ctk.CTkFrame(self.entries_frame, fg_color="#1c1c1c", corner_radius=14)
            row.pack(fill="x", padx=15, pady=8)

            row.grid_columnconfigure(0, weight=2)
            row.grid_columnconfigure(1, weight=2)
            row.grid_columnconfigure(2, weight=1)
            row.grid_columnconfigure(3, weight=1)
            row.grid_columnconfigure(4, weight=1)
            row.grid_columnconfigure(5, weight=0)

            ctk.CTkLabel(row, text=website, width=260, anchor="w").grid(row=0, column=0, padx=10, pady=16, sticky="w")
            ctk.CTkLabel(row, text=username, width=270, anchor="w").grid(row=0, column=1, padx=10, sticky="w")
            ctk.CTkLabel(row, text=shown_password, width=160, anchor="w").grid(row=0, column=2, padx=5, sticky="w")
            ctk.CTkLabel(row, text=category or "", width=130, anchor="w").grid(row=0, column=3, padx=5, sticky="w")
            ctk.CTkLabel(row, text=notes or "", width=160, anchor="w").grid(row=0, column=4, padx=5, sticky="w")

            btn_frame = ctk.CTkFrame(row, fg_color="transparent")
            btn_frame.grid(row=0, column=5, padx=(0, 10), pady=10, sticky="e")

            ctk.CTkButton(
                btn_frame,
                text="Copy",
                width=60,
                height=34,
                fg_color="#222222",
                hover_color="#333333",
                command=lambda p=password: self.copy_password(p)# Passwort kopieren
            ).pack(side="left", padx=2)

            ctk.CTkButton(
                btn_frame,
                text="Edit",
                width=60,
                height=34,
                fg_color="#333333",
                hover_color="#444444",
                command=lambda eid=entry_id, w=website, u=username, p=password, c=category, n=notes:
                self.edit_entry(eid, w, u, p, c, n)
            ).pack(side="left", padx=4)

            ctk.CTkButton(
                btn_frame,
                text="Del",
                width=55,
                height=34,
                fg_color="#E5E5E5",
                hover_color="#F5F5F5",
                text_color="black",
                command=lambda eid=entry_id: self.delete_entry(eid)# Eintrag löschen
            ).pack(side="left", padx=4)

    def toggle_passwords(self):# Wechselt zwischen sichtbar/versteckt
        self.passwords_visible = not self.passwords_visible# True wird False und umgekehrt

        if self.passwords_visible:
            self.show_button.configure(text="Passwörter verstecken")
        else:
            self.show_button.configure(text="Passwörter anzeigen")

        self.refresh_entries()

    def delete_entry(self, entry_id):# Öffnet Bestätigungsfenster zum Löschen
        dialog = ctk.CTkToplevel(self.master)
        dialog.title("Löschen")
        dialog.geometry("360x200")
        dialog.configure(fg_color="#0b0b0b")
        dialog.resizable(False, False)

        dialog.lift()
        dialog.focus_force()
        dialog.grab_set()

        ctk.CTkLabel(
            dialog,
            text="Eintrag wirklich löschen?",
            font=("Arial", 20),
            text_color="#e50914"
        ).pack(pady=35)

        button_frame = ctk.CTkFrame(dialog, fg_color="transparent")
        button_frame.pack(pady=10)

        def confirm_delete():# Löscht Eintrag aus der Datenbank
            self.db.delete_entry(entry_id)
            self.refresh_entries()
            dialog.destroy()

        ctk.CTkButton(
            button_frame,
            text="Ja",
            command=confirm_delete,
            fg_color="#e50914",
            hover_color="#ff1a25",
            width=120,
            height=40
        ).grid(row=0, column=0, padx=10)

        ctk.CTkButton(
            button_frame,
            text="Nein",
            command=dialog.destroy,
            fg_color="#222222",
            hover_color="#333333",
            width=120,
            height=40
        ).grid(row=0, column=1, padx=10)

    def copy_password(self, password):# Kopiert Passwort in Zwischenablage
        self.master.clipboard_clear()
        self.master.clipboard_append(password)

    def edit_entry(self, entry_id, old_website, old_username, old_password, old_category="", old_notes=""): # Formular zum Bearbeiten öffnen
        form = ctk.CTkToplevel(self.master)
        form.lift()
        form.focus_force()
        form.grab_set()
        form.title("Eintrag bearbeiten")
        form.geometry("600x700")
        form.configure(fg_color="#0b0b0b")
        form.resizable(False, False)

        ctk.CTkLabel(form, text="Eintrag bearbeiten", font=("Arial", 26), text_color="#e50914").pack(pady=25)

        ctk.CTkLabel(form, text="Website", text_color="#e50914", font=("Arial", 14, "bold")).pack(anchor="w", padx=150)
        website_entry = ctk.CTkEntry(form, width=300, height=40)
        website_entry.insert(0, old_website)# Vorhandene Werte einfügen
        website_entry.pack(pady=8)

        ctk.CTkLabel(form, text="Benutzername", text_color="#e50914", font=("Arial", 14, "bold")).pack(anchor="w", padx=150)
        username_entry = ctk.CTkEntry(form, width=300, height=40)
        username_entry.insert(0, old_username)
        username_entry.pack(pady=8)

        ctk.CTkLabel(form, text="Passwort", text_color="#e50914", font=("Arial", 14, "bold")).pack(anchor="w", padx=150)
        password_entry = ctk.CTkEntry(form, width=300, height=40)
        password_entry.insert(0, old_password)
        password_entry.pack(pady=8)

        ctk.CTkLabel(form, text="Kategorie", text_color="#e50914").pack(anchor="w", padx=150)
        category_entry = ctk.CTkEntry(form, width=300, height=40)
        category_entry.insert(0, old_category or "")
        category_entry.pack(pady=5)

        ctk.CTkLabel(form, text="Notizen", text_color="#e50914").pack(anchor="w", padx=150)
        notes_entry = ctk.CTkEntry(form, width=300, height=40)
        notes_entry.insert(0, old_notes or "")
        notes_entry.pack(pady=5)

        def save_changes():
            website = website_entry.get().strip()
            username = username_entry.get().strip()
            password = password_entry.get().strip()
            category = category_entry.get().strip()
            notes = notes_entry.get().strip()

            if website == "" or username == "" or password == "":
                messagebox.showwarning("Fehler", "Bitte alle Pflichtfelder ausfüllen.")
                return

            self.db.update_entry(entry_id, website, username, password, category, notes)# Datenbankeintrag aktualisieren
            self.refresh_entries()
            form.destroy()

        ctk.CTkButton(
            form,
            text="Änderungen speichern",
            command=save_changes,
            fg_color="#e50914",
            hover_color="#ff1a25",
            width=220,
            height=45
        ).pack(pady=25)

    def check_password_strength(self, password):
        score = 0

        if len(password) >= 8:
            score += 1

        if any(char.isdigit() for char in password):
            score += 1

        if any(char.isupper() for char in password):
            score += 1

        if any(char in "!@#$%^&*()-_?" for char in password):
             score += 1

        if score <= 1:
            return "Schwach", "red"
        elif score <= 3:
            return "Mittel", "orange"
        else:
            return "Stark", "green"

    def open_new_entry_form(self): # Formular für neuen Eintrag öffnen
        form = ctk.CTkToplevel(self.master)
        form.lift()
        form.focus_force()
        form.grab_set()
        form.title("Neuer Eintrag")
        form.geometry("600x700")
        form.configure(fg_color="#0b0b0b")
        form.resizable(False, False)

        ctk.CTkLabel(
            form,
            text="Neuer Eintrag",
            font=("Arial", 26),
            text_color="#e50914"
        ).pack(pady=25)

        website_entry = ctk.CTkEntry(form, placeholder_text="Website", width=300, height=40)
        website_entry.pack(pady=8)

        username_entry = ctk.CTkEntry(form, placeholder_text="Benutzername", width=300, height=40)
        username_entry.pack(pady=8)

        password_entry = ctk.CTkEntry(form, placeholder_text="Passwort", width=300, height=40, show="*")
        password_entry.pack(pady=8)

        strength_label = ctk.CTkLabel(
            form,
            text="Passwortstärke: -",
            text_color="#E5E5E5"
        )
        strength_label.pack(pady=2)

        def update_strength(event=None):
            strength, color = self.check_password_strength(password_entry.get())

            strength_label.configure(
                text=f"Passwortstärke: {strength}",
                text_color=color
            )

        password_entry.bind("<KeyRelease>", update_strength)

        def generate_password(): # Zufälliges Passwort generieren
            generated_password = PasswordGenerator.generate()
            password_entry.delete(0, "end")
            password_entry.insert(0, generated_password)
            update_strength()

        ctk.CTkButton(
            form,
            text="Passwort generieren",
            command=generate_password,
            fg_color="#222222",
            hover_color="#333333",
            width=220,
            height=40
        ).pack(pady=8)

        category_entry = ctk.CTkEntry(form, placeholder_text="Kategorie", width=300, height=40)
        category_entry.pack(pady=8)

        notes_entry = ctk.CTkEntry(form, placeholder_text="Notizen", width=300, height=40)
        notes_entry.pack(pady=8)

        def save_entry(): # Neuen Eintrag speichern
            website = website_entry.get().strip()
            username = username_entry.get().strip()
            password = password_entry.get().strip()
            category = category_entry.get().strip()
            notes = notes_entry.get().strip()

            if website == "" or username == "" or password == "":
                messagebox.showwarning("Fehler", "Bitte alle Felder ausfüllen.")
                return

            self.db.add_entry(website, username, password, category, notes)
            self.refresh_entries()
            form.destroy()

        ctk.CTkButton(
            form,
            text="Speichern",
            command=save_entry,
            fg_color="#e50914",
            hover_color="#ff1a25",
            width=220,
            height=45
        ).pack(pady=25)