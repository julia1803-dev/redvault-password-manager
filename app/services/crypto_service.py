from cryptography.fernet import Fernet # Wird für das Ver- und Entschlüsseln verwendet
import os # Modul für Datei- und Betriebssystemfunktionen
import hashlib # Modul für Hash-Funktionen

# Service-Klasse für Verschlüsselung
class CryptoService:
    def __init__(self, key_file="secret.key"):
        # Name der Datei, in der der Schlüssel gespeichert wird
        self.key_file = key_file

        # Lädt vorhandenen Schlüssel oder erstellt neuen
        self.key = self.load_or_create_key()
         # Erstellt Fernet-Objekt mit dem Schlüssel
        self.fernet = Fernet(self.key)
    # Lädt vorhandenen Schlüssel oder erstellt einen neuen
    def load_or_create_key(self):
        # Prüft, ob die Schlüsseldatei existiert
        if os.path.exists(self.key_file):
            # Öffnet Datei im Lese-Modus (rb = read binary)
            with open(self.key_file, "rb") as f:
                # Liest den gespeicherten Schlüssel
                return f.read()
        else:
            # Erstellt neuen Verschlüsselungsschlüssel
            key = Fernet.generate_key()
             # Speichert Schlüssel in Datei
            # wb = write binary
            with open(self.key_file, "wb") as f:
                f.write(key)
            return key
        
    # Verschlüsselt einen Text
    def encrypt(self, text: str) -> str:
        # encrypt() verschlüsselt den Text
        return self.fernet.encrypt(text.encode()).decode() # encode() wandelt Text in Bytes um
        # decode() macht daraus wieder lesbaren Text
    
    # Entschlüsselt einen Text
    def decrypt(self, encrypted_text: str) -> str:
       
        return self.fernet.decrypt(encrypted_text.encode()).decode()
    
    # Funktion zum Hashen des Master-Passworts
def hash_master_password(password, salt=None):
    if salt is None:
        salt = os.urandom(16) # Erstellt zufälligen Salt mit 16 Bytes

    password_hash = hashlib.pbkdf2_hmac( 
        "sha256",
        password.encode(), # Passwort als Bytes
        salt, # Zufälliger Salt
        100_000 # Anzahl Wiederholungen
    ) # Erstellt Passwort-Hash mit PBKDF2-HMAC

    return salt, password_hash # Gibt Salt und Hash zurück

# Überprüft Master-Passwort beim Login
def verify_master_password(password, salt, saved_hash):
         # Erstellt neuen Hash aus eingegebenem Passwort
        new_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode(),
            salt,
            100_000
        )
        # Vergleicht neuen Hash mit gespeichertem Hash
        return new_hash == saved_hash