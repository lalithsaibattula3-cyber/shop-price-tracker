import tkinter as tk
from tkinter import ttk

BG      = "#1a1f2e"
SURFACE = "#232a3d"
SURFACE2= "#2d3548"
ACCENT  = "#22c55e"
ORANGE  = "#f97316"
TEXT    = "#e8eaf0"
MUTED   = "#9ca3af"
GREEN   = "#22c55e"
RED     = "#ef4444"
BLUE    = "#3b82f6"
FONT    = ("Segoe UI", 10)
BOLD    = ("Segoe UI", 10, "bold")
TITLE   = ("Segoe UI", 15, "bold")
BIG     = ("Segoe UI", 22, "bold")

class Reports:
    def __init__(self, root, app):
        self.root = root
        self.app  = app
        self.frame = tk.Frame(root, bg=BG)
        self._build()

    def _build(self):
        f = self.frame

        nav = tk.Frame(f, bg=ORANGE, pady=8)
        nav.pack(fill="x")
        tk.Button(nav, text="← Back", command=self._back, bg="#c2540a", fg="white",
                  font=BOLD, relief="flat", cursor="hand2", padx=12, pady=3).pack(side="left", padx=12)
        tk.Label(nav, text="📊  Reports & Analytics", font=("Segoe UI",13,"bold"),
                 bg=ORANGE, fg="white").pack(side="left", padx=10)
        tk.Button(nav, text="↻ Refresh", command=self._load, bg="#374151", fg=TEXT,
                  font=FONT, relief="flat", cursor="hand2", padx=12, pady=3).pack(side="right", padx=12)

        body = tk.Frame(f, bg=BG)
        body.pack(fill="both", expand=True, padx=20, pady=16)

        # Summary cards row
        self.cards_frame = tk.Frame(body, bg=BG)
        self.cards_frame.pack(fill="x", pady=(0,16))

        self.card_vars = {}
        card_defs = [
            ("confirmed",   "✔  Confirmed",    GREEN),
            ("cancelled",   "✘  Cancelled",    RED),
            ("passengers",  "👥 Passengers",   BLUE),
            ("revenue",     "₹  Revenue",      ORANGE),
        ]
        for key, label, color in card_defs:
            card = tk.Frame(self.cards_frame, bg=SURFACE, padx=20, pady=16,
                            highlightthickness=2, highlightbackground=color)
            card.pack(side="left", expand=True, fill="both", padx=6)
            tk.Label(card, text=label, font=FONT, bg=SURFACE, fg=MUTED).pack(anchor="w")
            var = tk.StringVar(value="—")
            self.card_vars[key] = var
            tk.Label(card, textvariable=var, font=BIG, bg=SURFACE, fg=color).pack(anchor="w", pady=4)

        # Train report table
        tk.Label(body, text="Train-wise Report", font=TITLE, bg=BG, fg=TEXT).pack(anchor="w", pady=(10,6))

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Rep.Treeview", background=SURFACE, foreground=TEXT,
                        fieldbackground=SURFACE, rowheight=28, font=FONT)
        style.configure("Rep.Treeview.Heading", background=SURFACE2, foreground=ACCENT,
                        font=BOLD, relief="flat")
        style.map("Rep.Treeview", background=[("selected","#374151")])

        cols = ("Train Code","Train Name","Bookings","Passengers","Revenue (₹)")
        self.tree = ttk.Treeview(body, columns=cols, show="headings",
                                 style="Rep.Treeview", height=12)
        widths = [90, 280, 100, 110, 120]
        for col, w in zip(cols, widths):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=w, anchor="center")
        self.tree.pack(fill="both", expand=True)

        vsb = ttk.Scrollbar(body, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)

    def _load(self):
        summary = self.app.report_service.get_summary()
        self.card_vars["confirmed"].set(str(summary["confirmed"]))
        self.card_vars["cancelled"].set(str(summary["cancelled"]))
        self.card_vars["passengers"].set(str(summary["passengers"]))
        self.card_vars["revenue"].set(f"₹{summary['revenue']:,}")

        self.tree.delete(*self.tree.get_children())
        train_report = self.app.report_service.get_train_report()
        for r in train_report:
            name, code, bookings, pax, rev = r
            self.tree.insert("", "end", values=(code, name, bookings, pax, f"₹{rev:,}"))

    def _back(self):
        self.hide()
        self.app.main_menu.show()

    def show(self):
        self._load()
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()
