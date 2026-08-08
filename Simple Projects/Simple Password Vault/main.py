#!/usr/bin/env python3
"""
Simple Password Vault
A local, encrypted password manager (CLI).

Uses a master password to derive an encryption key (PBKDF2 + Fernet/AES).
All entries are stored encrypted in a local JSON file (vault.dat).
"""

import os
import sys
import json
import base64
import getpass
import time
import subprocess


def ensure_cryptography_installed():
    """Check if 'cryptography' is installed, install it if missing."""
    check = subprocess.run(
        [sys.executable, "-m", "pip", "show", "cryptography"],
        capture_output=True,
        text=True
    )
    if check.returncode == 0:
        return
    print("Installing required dependency 'cryptography'...")
    subprocess.run([sys.executable, "-m", "pip", "install", "cryptography"], check=True)
    time.sleep(1)


# Must happen BEFORE importing cryptography, otherwise the import itself
# crashes the script if the package isn't installed yet.
ensure_cryptography_installed()

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

VAULT_FILE = "vault.dat"
SALT_FILE = "vault.salt"
ITERATIONS = 390_000


def derive_key(master_password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=ITERATIONS,
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
    return key


def get_or_create_salt() -> bytes:
    if os.path.exists(SALT_FILE):
        with open(SALT_FILE, "rb") as f:
            return f.read()
    salt = os.urandom(16)
    with open(SALT_FILE, "wb") as f:
        f.write(salt)
    return salt


def load_vault(fernet: Fernet) -> dict:
    if not os.path.exists(VAULT_FILE):
        return {}
    with open(VAULT_FILE, "rb") as f:
        encrypted = f.read()
    if not encrypted:
        return {}
    try:
        decrypted = fernet.decrypt(encrypted)
        return json.loads(decrypted.decode())
    except InvalidToken:
        print("❌ Wrong master password or corrupted vault.")
        sys.exit(1)


def save_vault(fernet: Fernet, data: dict):
    encrypted = fernet.encrypt(json.dumps(data).encode())
    with open(VAULT_FILE, "wb") as f:
        f.write(encrypted)


def add_entry(vault: dict):
    site = input("Site/App name: ").strip()
    username = input("Username/Email: ").strip()
    password = getpass.getpass("Password (leave blank to auto-generate): ").strip()
    if not password:
        password = generate_password()
        print(f"Generated password: {password}")
    vault[site] = {"username": username, "password": password}
    print(f"✅ Saved entry for '{site}'.")


def get_entry(vault: dict):
    site = input("Site/App name to look up: ").strip()
    entry = vault.get()
    if not entry:
        print("❌ No entry found.")
        return
    print(f"\nSite:     {site}")
    print(f"Username: {entry['username']}")
    print(f"Password: {entry['password']}\n")


def list_entries(vault: dict):
    if not vault:
        print("Vault is empty.")
        return
    print("\nStored sites:")
    for site in vault:
        print(f"  - {site}")
    print()


def delete_entry(vault: dict):
    site = input("Site/App name to delete: ").strip()
    if site in vault:
        del vault[site]
        print(f"🗑️ Deleted entry for '{site}'.")
    else:
        print("❌ No entry found.")


def generate_password(length: int = 16) -> str:
    import secrets
    import string
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    return "".join(secrets.choice(alphabet) for _ in range(length))


def main():
    print("=== Simple Password Vault ===")
    salt = get_or_create_salt()
    master_password = getpass.getpass("Master password: ")
    key = derive_key(master_password, salt)
    fernet = Fernet(key)
    vault = load_vault(fernet)

    menu = """
1. Add entry
2. Get entry
3. List sites
4. Delete entry
5. Save & Exit
"""
    while True:
        print(menu)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_entry(vault)
            save_vault(fernet, vault)
        elif choice == "2":
            get_entry(vault)
        elif choice == "3":
            list_entries(vault)
        elif choice == "4":
            delete_entry(vault)
            save_vault(fernet, vault)
        elif choice == "5":
            save_vault(fernet, vault)
            print("Vault saved. Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()