import customtkinter as ctk
from PIL import Image
from tkinter import messagebox
from app.database.database import Database


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

db = Database()
passwords_visible = False


def refresh_entries():
    for widget in entries_frame.winfo_children():
        widget.destroy()

    entries = db.get_entries()

    for entry in entries:
        entry_id = entry[0]
        website = entry[1]
        username = entry[2]
        password = entry[3]

        shown_password = password if passwords_visible else "••••••••"

        row = ctk.CTkFrame(entries_frame, fg_color="#1c1c1c", corner_radius=14)
        row.pack(fill="x", padx=15, pady=8)

        row.grid_columnconfigure(0, weight=2)   # Website
        row.grid_columnconfigure(1, weight=1)   # Username kleiner!
        row.grid_columnconfigure(2, weight=1)   # Passwort näher ran
        row.grid_columnconfigure(3, weight=0)

        ctk.CTkLabel(row, text=website, width=370, anchor="w").grid(row=0, column=0, padx=20, pady=16, sticky="w")
        ctk.CTkLabel(row, text=username, width=330, anchor="w").grid(row=0, column=1, padx=20, sticky="w")
        ctk.CTkLabel(row, text=shown_password, width=220, anchor="w").grid(row=0, column=2, padx=5, sticky="w")
        btn_frame = ctk.CTkFrame(row, fg_color="transparent")
        btn_frame.grid(row=0, column=3, padx=25, pady=10)

        ctk.CTkButton(
            btn_frame,
            text="Copy",
            width=60,
            height=34,
            fg_color="#222222",
            hover_color="#333333",
            command=lambda p=password: copy_password(p)
        ).pack(side="left", padx=4)

        ctk.CTkButton(
            btn_frame,
            text="Edit",
            width=60,
            height=34,
            fg_color="#333333",
            hover_color="#444444",
            command=lambda eid=entry_id, w=website, u=username, p=password: edit_entry(eid, w, u, p)
        ).pack(side="left", padx=4)

        ctk.CTkButton(
            btn_frame,
            text="Del",
            width=55,
            height=34,
            fg_color="#E5E5E5",
            hover_color="#F5F5F5",
            text_color="black",
            command=lambda eid=entry_id: delete_entry(eid)
        ).pack(side="left", padx=4)


def toggle_passwords():
    global passwords_visible
    passwords_visible = not passwords_visible

    if passwords_visible:
        show_button.configure(text="Passwörter verstecken")
    else:
        show_button.configure(text="Passwörter anzeigen")

    refresh_entries()


def delete_entry(entry_id):
    dialog = ctk.CTkToplevel(root)
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

    def confirm_delete():
        db.delete_entry(entry_id)
        refresh_entries()
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


def copy_password(password):
    root.clipboard_clear()
    root.clipboard_append(password)


def edit_entry(entry_id, old_website, old_username, old_password):
    form = ctk.CTkToplevel(root)
    form.lift()
    form.focus_force()
    form.grab_set()
    form.title("Eintrag bearbeiten")
    form.geometry("420x420")
    form.configure(fg_color="#0b0b0b")
    form.resizable(False, False)

    ctk.CTkLabel(
        form,
        text="Eintrag bearbeiten",
        font=("Arial", 26),
        text_color="#e50914"
    ).pack(pady=25)

    website_entry = ctk.CTkEntry(form, width=300, height=40)
    website_entry.insert(0, old_website)
    website_entry.pack(pady=8)

    username_entry = ctk.CTkEntry(form, width=300, height=40)
    username_entry.insert(0, old_username)
    username_entry.pack(pady=8)

    password_entry = ctk.CTkEntry(form, width=300, height=40)
    password_entry.insert(0, old_password)
    password_entry.pack(pady=8)

    def save_changes():
        website = website_entry.get().strip()
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if website == "" or username == "" or password == "":
            messagebox.showwarning("Fehler", "Bitte alle Felder ausfüllen.")
            return

        db.update_entry(entry_id, website, username, password)
        refresh_entries()
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


def open_new_entry_form():
    form = ctk.CTkToplevel(root)
    form.lift()
    form.focus_force()
    form.grab_set()
    form.title("Neuer Eintrag")
    form.geometry("420x420")
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

    def save_entry():
        website = website_entry.get().strip()
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if website == "" or username == "" or password == "":
            messagebox.showwarning("Fehler", "Bitte alle Felder ausfüllen.")
            return

        db.add_entry(website, username, password)
        refresh_entries()
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


root = ctk.CTk()
logo_image = ctk.CTkImage(
    light_image=Image.open("assets/logo.png"),
    dark_image=Image.open("assets/logo.png"),
    size=(40, 40)  # 👈 Größe anpassen
)
root.title("RedVault Passwortmanager")
root.geometry("1000x650")
root.configure(fg_color="#0b0b0b")

title_frame = ctk.CTkFrame(root, fg_color="transparent")
title_frame.pack(pady=25)

# LOGO
ctk.CTkLabel(
    title_frame,
    image=logo_image,
    text=""
).pack(side="left", padx=(0, 8))  # 👈 Abstand perfekt

# RED
ctk.CTkLabel(
    title_frame,
    text="RED",
    font=("Arial", 42, "bold"),
    text_color="#e50914"
).pack(side="left")

# VAULT
ctk.CTkLabel(
    title_frame,
    text="VAULT",
    font=("Arial", 42, "bold"),
    text_color="#E5E5E5"
).pack(side="left")

button_frame = ctk.CTkFrame(root, fg_color="transparent")
button_frame.pack(pady=10)

ctk.CTkButton(
    button_frame,
    text="+ Neuer Eintrag",
    command=open_new_entry_form,
    fg_color="#e50914",
    hover_color="#ff1a25",
    width=200,
    height=45
).grid(row=0, column=0, padx=10)

show_button = ctk.CTkButton(
    button_frame,
    text="Passwörter anzeigen",
    command=toggle_passwords,
    fg_color="#222222",
    hover_color="#333333",
    width=200,
    height=45
)
show_button.grid(row=0, column=1, padx=10)

container = ctk.CTkFrame(root, fg_color="#e50914", corner_radius=16)
container.pack(padx=40, pady=30, fill="both", expand=True)

inner = ctk.CTkFrame(container, fg_color="#101010", corner_radius=14)
inner.pack(padx=2, pady=2, fill="both", expand=True)

header = ctk.CTkFrame(inner, fg_color="#101010")
header.pack(fill="x", padx=25, pady=(10, 5))

header.grid_columnconfigure(0, weight=2)
header.grid_columnconfigure(1, weight=1)
header.grid_columnconfigure(2, weight=1)
header.grid_columnconfigure(3, weight=0)

ctk.CTkLabel(header, text="Website", text_color="#e50914", width=370, anchor="w").grid(row=0, column=0, padx=20, sticky="w")
ctk.CTkLabel(header, text="Benutzername", text_color="#e50914", width=330, anchor="w").grid(row=0, column=1, padx=20, sticky="w")
ctk.CTkLabel(header, text="Passwort", text_color="#e50914", width=220, anchor="w").grid(row=0, column=2, padx=5, sticky="w")
ctk.CTkLabel(header, text="Aktionen", text_color="#e50914", width=200, anchor="w").grid(row=0, column=3, padx=25, sticky="w")

entries_frame = ctk.CTkScrollableFrame(inner, fg_color="#101010")
entries_frame.pack(fill="both", expand=True, padx=10, pady=10)

refresh_entries()

root.mainloop()