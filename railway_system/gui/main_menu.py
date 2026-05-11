import tkinter as tk
from tkinter import messagebox

BG      = "#1a1f2e"
SURFACE = "#232a3d"
SURFACE2= "#2d3548"
ACCENT  = "#f97316"
TEXT    = "#e8eaf0"
MUTED   = "#9ca3af"
FONT    = ("Segoe UI", 10)
BOLD    = ("Segoe UI", 11, "bold")
TITLE   = ("Segoe UI", 18, "bold")

class MainMenu:
    def __init__(self, root, app):
        self.root = root
        self.app  = app
        self.frame = tk.Frame(root, bg=BG)
        self._build()

    def _build(self):
        f = self.frame

        # Top navbar
        nav = tk.Frame(f, bg=ACCENT, pady=10)
        nav.pack(fill="x")
        tk.Label(nav, text="🚆  Smart Railway Reservation System", font=("Segoe UI", 14, "bold"),
                 bg=ACCENT, fg="white").pack(side="left", padx=20)
        self.user_label = tk.Label(nav, text="", font=FONT, bg=ACCENT, fg="white")
        self.user_label.pack(side="right", padx=10)
        tk.Button(nav, text="Logout", font=FONT, bg="#c2540a", fg="white", relief="flat",
                  cursor="hand2", padx=12, command=self._logout).pack(side="right", padx=10)

        # Content
        content = tk.Frame(f, bg=BG)
        content.pack(expand=True, fill="both")

        tk.Label(content, text="What would you like to do?", font=TITLE, bg=BG, fg=TEXT).pack(pady=(40, 10))
        tk.Label(content, text="Select an option below", font=FONT, bg=BG, fg=MUTED).pack(pady=(0, 30))

        # Menu buttons grid
        grid = tk.Frame(content, bg=BG)
        grid.pack()

        buttons = [
            ("🔍", "Search & Book Train", "#f97316", self._go_booking),
            ("📋", "PNR Status", "#3b82f6", self._go_pnr),
            ("❌", "Cancel Ticket", "#ef4444", self._go_cancel),
            ("📊", "Reports", "#22c55e", self._go_reports),
        ]

        for i, (icon, label, color, cmd) in enumerate(buttons):
            card = tk.Frame(grid, bg=SURFACE, padx=30, pady=25,
                            highlightthickness=2, highlightbackground=color, cursor="hand2")
            card.grid(row=i//2, column=i%2, padx=16, pady=16)
            tk.Label(card, text=icon, font=("Segoe UI", 36), bg=SURFACE).pack()
            tk.Label(card, text=label, font=BOLD, bg=SURFACE, fg=TEXT).pack(pady=8)
            tk.Button(card, text="Open →", font=FONT, bg=color, fg="white",
                      relief="flat", padx=16, pady=4, cursor="hand2", command=cmd).pack()

        # Admin panel button
        self.admin_btn = tk.Button(content, text="⚙  Admin Panel", font=FONT, bg=SURFACE2, fg=TEXT,
                                   relief="flat", padx=16, pady=6, cursor="hand2",
                                   command=self._go_admin)
        # shown only for admin

    def _go_booking(self):
        self.hide()
        self.app.train_booking.show()

    def _go_pnr(self):
        self.hide()
        self.app.pnr_status.show()

    def _go_cancel(self):
        self.hide()
        self.app.cancellation.show()

    def _go_reports(self):
        self.hide()
        self.app.reports.show()

    def _go_admin(self):
        self.hide()
        self.app.admin_panel.show()

    def _logout(self):
        self.app.current_user = None
        self.hide()
        self.app.login_screen.show()

    def show(self):
        u = self.app.current_user
        self.user_label.config(text=f"👤 {u['username']}  ({u['role']})")
        if u["role"] == "admin":
            self.admin_btn.pack(pady=10)
        else:
            self.admin_btn.pack_forget()
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()
