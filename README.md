# 🔐 RedVault – Password Manager

RedVault ist ein lokaler Passwortmanager für Websites, entwickelt in Python.  
Die Anwendung ermöglicht das sichere Speichern, Verwalten und Generieren von Passwörtern.

## Features

- Master-Passwort Login
- Verschlüsselte Speicherung von Passwörtern
- CRUD-Funktionen (Erstellen, Anzeigen, Bearbeiten, Löschen)
- Suche nach Website / Benutzername
- Passwortgenerator
- Kategorien für Einträge
- Einfaches, dunkles UI (CustomTkinter)

## Technologien

- Python 3.x
- CustomTkinter (GUI)
- SQLite (Datenbank)
- Cryptography (Verschlüsselung)

---

## Installation

### 1. Repository klonen
git clone https://github.com/DEIN_USERNAME/redvault-password-manager.git
cd redvault-password-manager

2. Virtuelle Umgebung erstellen
python -m venv venv

3. Umgebung aktivieren
Windows:
venv\Scripts\activate

4. Abhängigkeiten installieren
pip install -r requirements.txt

▶Programm starten
py main.py

Sicherheit
Master-Passwort wird nicht im Klartext gespeichert
Schlüssel wird aus Passwort abgeleitet (PBKDF2 oder Argon2)
Alle Daten werden verschlüsselt gespeichert (AES)

Projektstruktur
redvault/
│
├── main.py
├── README.md
├── requirements.txt
│
├── app/
│   ├── models/
│   ├── services/
│   ├── database/
│   └── ui/

Erweiterungen (optional)
Favoriten
Papierkorb
Passwortstärke-Anzeige
Auto-Lock
Backup / Export
Zwischenablage löschen