from tkinter import ttk

def _configure_styles(self):
        style = ttk.Style(self)

        # Tema base (clam suele respetar mejor los colores custom)
        style.theme_use("clam")

        # ====== FRAMES ======
        style.configure(
            "TFrame",
            background=self.CARD_BG,
        )

        # ====== LABELS ======
        style.configure(
            "TLabel",
            background=self.CARD_BG,
            foreground=self.TEXT_MAIN,
            font=("Segoe UI", 10)
        )

        # Label especial tipo “título”
        style.configure(
            "Title.TLabel",
            background=self.CARD_BG,
            foreground=self.ACCENT,
            font=("Segoe UI", 12, "bold")
        )

        # ====== CHECKBUTTONS ======
        style.configure(
            "TCheckbutton",
            background=self.CARD_BG,
            foreground=self.TEXT_MAIN,
            font=("Segoe UI", 9)
        )

        # ====== ENTRY / SPINBOX ======
        style.configure(
            "TEntry",
            fieldbackground="#020617",
            background=self.TEXT_MAIN,
            foreground=self.TEXT_MAIN,
            borderwidth=1,
            relief="flat"
        )
        style.configure(
            "TSpinbox",
            fieldbackground="#020617",
            background="#020617",
            foreground=self.TEXT_MAIN,
            arrowsize=12,
            borderwidth=1,
            relief="flat"
        )

        # ====== BOTONES ======
        # Botón por defecto (secundario)
        style.configure(
            "TButton",
            background=self.ACCENT_HOVER,
            foreground=self.TEXT_MAIN,
            font=("Segoe UI", 10, "bold"),
            padding=(12, 6),
            borderwidth=0
        )

        # Botón principal con acento (el de "Generate Password")
        style.configure(
            "Accent.TButton",
            background=self.ACCENT,
            foreground=self.CARD_BG,
            font=("Segoe UI", 10, "bold"),
            padding=(12, 6),
            borderwidth=0
        )

        style.map(
            "Accent.TButton",
            background=[
                ("active", self.ACCENT_HOVER),
                ("pressed", self.ACCENT_HOVER)
            ],
            foreground=[
                ("disabled", self.TEXT_MUTED)
            ]
        )
        
        style.map(
            "TCheckbutton",
            background=[
                ("active", self.CARD_BG),
                ("pressed", self.CARD_BG)
            ],
            foreground=[
                ("disabled", self.CARD_BG)
            ]
        )