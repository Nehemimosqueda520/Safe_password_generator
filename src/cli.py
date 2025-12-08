import tkinter as tk
from tkinter import messagebox
from build_ui import _build_ui
from style import _configure_styles

from config import (
    DEFAULT_PASSWORD_LENGTH,
    DEFAULT_USE_DIGITS,
    DEFAULT_USE_SPECIAL_CHARS,
    DEFAULT_USE_UPPERCASE,
)
from password_generator import generate_password

class PasswordGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Safe Password Generator")
        self.resizable(False, False)
        
        self.PRIMARY_BG = "#8B1414"   
        self.CARD_BG    = "#8B1414"   
        self.ACCENT     = "#3a6b7c"   
        self.ACCENT_HOVER = "#DB1A1A"
        self.TEXT_MAIN  = "#DAB5AA"   
        self.TEXT_MUTED = "#6e99df"  
        
        

        # Fondo de la ventana
        self.configure(bg=self.PRIMARY_BG)
        _configure_styles(self)

        self.length_var = tk.IntVar(value=DEFAULT_PASSWORD_LENGTH)
        self.use_uppercase_var = tk.BooleanVar(value=DEFAULT_USE_UPPERCASE)
        self.use_digits_var = tk.BooleanVar(value=DEFAULT_USE_DIGITS)
        self.use_special_chars_var = tk.BooleanVar(value=DEFAULT_USE_SPECIAL_CHARS)
        self.password_var = tk.StringVar()

        _build_ui(self)
        
    def generate_password(self):
        try:
            password = generate_password(
                length=self.length_var.get(),
                use_uppercase=self.use_uppercase_var.get(),
                use_digits=self.use_digits_var.get(),
                use_special_chars=self.use_special_chars_var.get(),
            )
        except ValueError as exc:
            self.password_var.set("")
            messagebox.showerror("Error", str(exc))
            return

        self.password_var.set(password)
        self.clipboard_clear()  