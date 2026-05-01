Projekt im Rahmen des HF Moduls OOP & Softwarearchitektur.

---# Konzept – RedVault Passwortmanager

## 1. Projektidee

RedVault ist ein lokaler Passwortmanager zur sicheren Verwaltung von Website-Logins.  
Ziel ist es, Passwörter verschlüsselt zu speichern und einfach zugänglich zu machen.

---

## 2. Zielsetzung

### Minimalziel
- Login mit Master-Passwort
- Speicherung von Website-Passwörtern
- CRUD-Funktionen
- Verschlüsselte Speicherung
- SQLite-Datenbank
- Passwortgenerator

### Erweiterte Ziele
- Kategorien
- Favoriten
- Papierkorb
- Passwortstärke
- Auto-Lock
- Backup/Export

---

## 3. Technologien

- Python
- CustomTkinter
- SQLite
- Cryptography

---

## 4. Architektur

Die Anwendung folgt einer klaren Schichtenarchitektur:
UI (CustomTkinter)
↓
Vault Service (Business Logic)
↓
Crypto Service (Verschlüsselung)
↓
SQLite Datenbank


---

## 5. OOP-Struktur

### Klassen

- `PasswordEntry`
- `VaultService`
- `CryptoService`
- `Database`
- `PasswordRepository`
- `PasswordGenerator`

---

## 6. Sicherheitskonzept

- Master-Passwort als Zugang
- Schlüsselableitung (PBKDF2 oder Argon2)
- AES-Verschlüsselung der Daten
- Keine Speicherung von Klartext-Passwörtern

---

## 7. Datenhaltung

- SQLite-Datenbank
- Strukturierte Speicherung der Einträge
- Automatische Erstellung der Datenbank beim Start

---

## 8. Benutzeroberfläche

- CustomTkinter
- Dunkles Design
- Fokus auf Funktionalität (kein komplexes UI)

---

## 9. Installierbarkeit

Das Projekt ist so aufgebaut, dass es von einer Drittperson lokal ausgeführt werden kann:

1. Repository klonen
2. Abhängigkeiten installieren
3. Programm starten

Alle benötigten Pakete sind in `requirements.txt` definiert.

---

## 10. Bewertungskriterien

- Saubere OOP-Struktur
- Trennung von Logik, UI und Datenbank
- Funktionierende Anwendung
- Dokumentation
- GitHub-Verlauf (Commits)