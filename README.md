# Safe Password Generator

Simple Tkinter desktop app to generate secure passwords based on user-selected options. Includes basic validation, custom styles, and helpers to measure entropy.

## Key features
- Generate random passwords combining lowercase, uppercase, digits, and special characters.
- Validate minimum length and ensure no forbidden characters are present before accepting the generated password.
- Lightweight GUI with controls for length and character set selection.
- Helper function to compute the Shannon entropy of any string.

## Project structure
- `src/main.py`: entry point that launches the `PasswordGeneratorApp`.
- `src/cli.py`: defines the main window, manages UI state, and coordinates password generation.
- `src/build_ui.py`: creates widgets (Spinbox, Checkbuttons, buttons) and arranges them in the window.
- `src/style.py`: configures Tkinter styles used in the interface.
- `src/password_generator.py`: builds the allowed character set and generates passwords using `secrets`.
- `src/validators.py`: checks that a password meets the minimum length and excludes invalid characters.
- `src/config.py`: configuration constants (default length, forbidden characters, etc.).
- `src/entropy.py`: calculates Shannon entropy for any string.

## Requirements
- Python 3.10+
- Dependencies listed in `requirements.txt` (Tkinter ships with most Python installations).

Install optional dependencies (formatting/binary helpers) with:
```bash
pip install -r requirements.txt
```
Windows:
```powershell
pip install -r requirements.txt
```

## Run the app
Run directly with Python:
```bash
python src/main.py
```
Windows (PowerShell or cmd):
```powershell
python src/main.py
```

Choose your options, click **Generate Password**, and the password will be copied to the clipboard.

## Tests
Automated tests use `pytest`. Run the full suite with:
```bash
pytest
```
Windows (PowerShell or cmd):
```powershell
pytest
```
