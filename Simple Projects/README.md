# Simple Projects

This folder contains small Python projects showcasing basic utility applications.

## Projects

### 1. Developer Login Checker
- File: `Developer Login Checker.py`
- Description: A simple login verifier that checks a user name against a predefined list and validates the associated ID.
- Notes: Demonstrates function arguments, lists, and basic conditional logic.

### 2. Simple Alarm Clock
- Folder: `Simple Alarm Clock/`
- Entry: `main.py`
- Description: A console-based alarm clock that accepts a time in `HH:MM` format and waits until the alarm time to ring.
- Notes: Uses `datetime`, `time`, and cross-platform audio fallback for alerts.

### 3. Simple Password Vault
- Folder: `Simple Password Vault/`
- Entry: `main.py`
- Description: A local password manager using a master password and encryption to store credentials securely.
- Notes: Uses `cryptography` for Fernet encryption, JSON storage, and a command-line menu for add/get/list/delete actions.

### 4. Student Notes Manager
- Folder: `Student Notes Manager/`
- Entry: `main.py`
- Description: A notebook utility for adding, displaying, searching, and counting notes in a local text file.
- Notes: Uses file I/O with `pathlib.Path`, plus simple menu-driven interaction.

## How to Use
1. Open a terminal in the `Simple Projects` folder.
2. Run the project you want:
   - `python "Developer Login Checker.py"`
   - `python "Simple Alarm Clock\main.py"`
   - `python "Simple Password Vault\main.py"`
   - `python "Student Notes Manager\main.py"`

## Requirements
- Most projects use only Python standard library modules.
- `Simple Password Vault` requires the `cryptography` package. The script attempts to install it automatically if missing.

## Notes
- `Student Notes Manager` stores notes in `notes.txt` inside its folder.
- `Simple Password Vault` stores encrypted vault data in `vault.dat` and `vault.salt`.
- `Simple Alarm Clock` expects a 24-hour time string like `07:30`.
