Projekt im Rahmen des HF Moduls OOP & Softwarearchitektur.

---# Konzept – RedVault Passwortmanager

# 1. Projektidee

RedVault ist ein lokaler Passwortmanager zur sicheren Verwaltung von Website-Logins.  
Ziel ist es, Passwörter verschlüsselt zu speichern und einfach zugänglich zu machen.


# 2. Zielsetzung

## Umgesetzte Ziele
- Login mit Master-Passwort
- Lokale Passwortverwaltung
- CRUD-Funktionen
- Passwortgenerator
- Kategorien für Einträge
- Passwortmaskierung
- Passwortstärke Anzeige
- Copy-to-Clipboard Funktion
- Suchfunktion
- Verschlüsselte Speicherung
- SQLite-Datenbank
- Dunkles UI mit CustomTkinter

## Erweiterte Ziele
- Favoriten-System
- Papierkorb
- Backup / Export
- Auto-Lock bei Inaktivität
- Cloud-Sync
- Katrgorie-Auswahl als Dropdown


# 3. Technologien

- Python
- CustomTkinter
- SQLite
- Cryptography


# 4. Architektur

Die Anwendung ist modular aufgebaut und trennt Darstellung, Geschäftslogik und Datenhaltung voneinander.
UI (CustomTkinter)
        ↓
VaultService
        ↓
CryptoService
        ↓
PasswordRepository
        ↓
SQLite Datenbank

Dadurch bleibt der Code wartbar, erweiterbar und übersichtlich.

# 5. OOP-Struktur

## Klassen

- PasswordEntry
- VaultService
- CryptoService
- Database
- PasswordRepository
- PasswordGenerator

## PasswordEntry
Repräsentiert einen Passwort-Eintrag mit:
- Website
- Benutzername
- Passwort
- Kategorie
- Notizen

# 6. Sicherheitskonzept

Die Anwendung speichert keine Passwörter im Klartext.

Sicherheitsmechanismen:
- Zugriff nur über Master-Passwort
- Verschlüsselte Speicherung sensibler Daten
- AES-Verschlüsselung mit der Cryptography Library
- Lokale Speicherung ohne Cloud-Anbindung
- Trennung von Logik und Datenzugriff
- Passwortstärke-Anzeige

# 7. Datenhaltung

Die Daten werden lokal in einer SQLite-Datenbank gespeichert.

Eigenschaften:
- automatische Erstellung der Datenbank beim ersten Start
- strukturierte Speicherung aller Einträge
- persistente Datenspeicherung

Zusätzlich wird ein geheimer Schlüssel in einer separaten Datei gespeichert.

## 8. Benutzeroberfläche

Die grafische Oberfläche wurde mit CustomTkinter entwickelt.

Merkmale:
- modernes Dark-Mode Design
- einfache Bedienung
- klare Struktur
- Fokus auf Benutzerfreundlichkeit

Fenster:
- Login
- Dashboard
- Neuer Eintrag
- Bearbeiten
- Löschen

# 9. Installierbarkeit

Das Projekt ist so aufgebaut, dass es von einer Drittperson lokal ausgeführt werden kann:

1. Repository klonen
2. Virtuelle Umgebung erstellen
3. Abhängigkeiten installieren
4. Anwendung starten

Alle benötigten Pakete sind in `requirements.txt` definiert.


# 10. Bewertungskriterien

Das Projekt fokussiert sich auf:

- saubere OOP-Struktur
- Trennung von Verantwortlichkeiten
- modulare Softwarearchitektur
- funktionierende GUI-Anwendung
- sichere Passwortspeicherung
- Dokumentation
- nachvollziehbaren GitHub-Verlauf