# 🔐 RedVault – Password Manager

RedVault ist ein lokaler Passwortmanager für Websites, entwickelt in Python.  
Die Anwendung ermöglicht das sichere Speichern, Verwalten und Generieren von Passwörtern.

## Features

- Master-Passwort Login
- AES-verschlüsselte Passwortspeicherung
- CRUD-Funktionen für Passwort-Einträge
- Suche nach Website oder Benutzername
- Passwortgenerator
- Kategorien für Einträge
- Bearbeiten bestehender Einträge
- Löschbestätigung vor dem Entfernen
- Passwortmaskierung
- Copy-to-Clipboard Funktion
- Modernes Dark-Mode UI mit CustomTkinter
- Lokale SQLite-Datenbank
- Modularer OOP-Aufbau

## Technologien

- Python 3.x
- CustomTkinter (GUI)
- SQLite (Datenbank)
- Cryptography (Verschlüsselung)
- Repository Pattern

## Architektur

Die Anwendung wurde nach OOP-Prinzipien entwickelt.

### Komponenten

- Models → Datenobjekte
- Services → Geschäftslogik
- Repository → Datenbankzugriffe
- UI → Benutzeroberfläche
- Security → Verschlüsselung & Authentifizierung

Das Projekt trennt Datenhaltung, Logik und Darstellung sauber voneinander.

## Sicherheit

- Master-Passwort wird nicht im Klartext gespeichert
- Verschlüsselung mit der Python Cryptography Library
- Sichere lokale Speicherung in SQLite
- AES-Verschlüsselung für sensible Daten
- Zugriff nur nach erfolgreichem Login

## Installation

### 1. Repository klonen
git clone https://github.com/julia1803-dev/redvault-password-manager
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


## Projektstruktur
redvault/
│
├── app/
│   ├── database/
│   │   ├── database.py
│   │   └── password_repository.py
│   │
│   ├── models/
│   │   └── password_entry.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── crypto_service.py
│   │   ├── password_generator.py
│   │   └── vault_service.py
│   │
│   ├── ui/
│   ├── app.py
│   └── config.py
│
├── assets/
│   └── logo.png
│
├── main.py
├── README.md
├── requirements.txt
├── vault.db
└── secret.key

## Geplante Erweiterungen

- Passwortstärke-Anzeige
- Auto-Lock bei Inaktivität
- Backup / Export
- Favoriten-System
- Papierkorb

## Screenshots

### Login
![Login]("C:\Tools\redvault\assets\Screeshot_Master_Passwort.png")

### Dashboard
![Dashboard]("C:\Tools\redvault\assets\Screenshot_Dashboard.png")

### Neuer Eintrag
![Neuer Eintrag]("C:\Tools\redvault\assets\Screenshot_Neuer_Eintrag.png")

### Bearbeiten
![Bearbeiten]("C:\Tools\redvault\assets\Screenshot_Bearbeiten.png")

### Löschen
![Löschen]("C:\Tools\redvault\assets\Screenshot_Löschen.png")