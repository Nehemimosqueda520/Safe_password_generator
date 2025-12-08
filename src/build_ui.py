from tkinter import ttk
from config import (
    MIN_PASSWORD_LENGTH,
)
from password_generator import generate_password

def _build_ui(self):
    main_frame = ttk.Frame(self, padding=16)
    main_frame.grid(row=0, column=0, sticky="nsew")

    length_label = ttk.Label(main_frame, text="Password length:")
    length_label.grid(row=0, column=0, sticky="w", pady=(0, 8))

    length_spinbox = ttk.Spinbox(
        main_frame,
        from_=MIN_PASSWORD_LENGTH,
        to=128,
        textvariable=self.length_var,
        width=6,
    )
    length_spinbox.grid(row=0, column=1, sticky="w", pady=(0, 8))

    uppercase_check = ttk.Checkbutton(
        main_frame,
        text="Include uppercase letters",
        variable=self.use_uppercase_var,
    )
    uppercase_check.grid(row=1, column=0, columnspan=2, sticky="w", pady=2)

    digits_check = ttk.Checkbutton(
        main_frame,
        text="Include digits",
        variable=self.use_digits_var,
    )
    digits_check.grid(row=2, column=0, columnspan=2, sticky="w", pady=2)

    special_chars_check = ttk.Checkbutton(
        main_frame,
        text="Include special characters",
        variable=self.use_special_chars_var,
    )
    special_chars_check.grid(row=3, column=0, columnspan=2, sticky="w", pady=2)

    generate_button = ttk.Button(
        main_frame, text="Generate Password", command=self.generate_password
    )
    generate_button.grid(row=4, column=0, columnspan=2, pady=(10, 6))

    password_label = ttk.Label(main_frame, text="Generated password:")
    password_label.grid(row=5, column=0, sticky="w")

    password_entry = ttk.Entry(
        main_frame,
        textvariable=self.password_var,
        width=40,
        state="readonly",
    )
    password_entry.grid(row=6, column=0, columnspan=2, sticky="we")

    self.columnconfigure(0, weight=1)
    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)