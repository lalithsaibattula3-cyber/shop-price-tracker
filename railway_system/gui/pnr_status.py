import tkinter as tk
from tkinter import messagebox

BG      = "#1a1f2e"
SURFACE = "#232a3d"
SURFACE2= "#2d3548"
ACCENT  = "#3b82f6"
TEXT    = "#e8eaf0"
MUTED   = "#9ca3af"
GREEN   = "#22c55e"
RED     = "#ef4444"
ORANGE  = "#f97316"
FONT    = ("Segoe UI", 10)
BOLD    = ("Segoe UI", 10, "bold")
TITLE   = ("Segoe UI", 15, "bold")
MONO    = ("Courier New", 11, "bold")

def btn(parent, text, cmd, bg=ACCENT):
    return tk.Button(parent, text=text, command=cmd, bg=bg, fg="white", font=BOLD,
                     relief="flat", cursor="hand2", padx=14, pady=5,
                     activebackground="#2563eb", activeforeground="white")

class PNRStatus:
    def __init__(self, root, app):
        self.root = root
        self.app  = app
        self.frame = tk.Frame(root, bg=BG)
        self._build()

    def _build(self):
        f = self.frame

        nav = tk.Frame(f, bg=ORANGE, pady=8)
        nav.pack(fill="x")
        btn(nav, "← Back", self._back, bg="#c2540a").pack(side="left", padx=12)
        tk.Label(nav, text="📋  PNR Status Check", font=("Segoe UI",13,"bold"),
                 bg=ORANGE, fg="white").pack(side="left", padx=10)

        body = tk.Frame(f, bg=BG)
        body.pack(expand=True, fill="both", padx=30, pady=30)

        # Search box
        sp = tk.Frame(body, bg=SURFACE, padx=30, pady=24,
                      highlightthickness=1, highlightbackground="#374151")
        sp.pack(fill="x")

        tk.Label(sp, text="Check PNR Status", font=TITLE, bg=SURFACE, fg=TEXT).pack(pady=(0,16))
        row = tk.Frame(sp, bg=SURFACE)
        row.pack()
        tk.Label(row, text="PNR Number:", font=FONT, bg=SURFACE, fg=MUTED).pack(side="left", padx=6)
        self.pnr_entry = tk.Entry(row, width=16, bg=SURFACE2, fg=TEXT, insertbackground=TEXT,
                                  font=MONO, relief="flat", highlightthickness=1,
                                  highlightcolor=ACCENT, highlightbackground="#374151")
        self.pnr_entry.pack(side="left", ipady=6, padx=8)
        btn(row, "CHECK STATUS", self._check).pack(side="left", padx=8)
        self.pnr_entry.bind("<Return>", lambda e: self._check())

        # Result card
        self.result_frame = tk.Frame(body, bg=SURFACE, padx=30, pady=24,
                                     highlightthickness=2, highlightbackground="#374151")

        # My bookings section
        my_hdr = tk.Frame(body, bg=BG)
        my_hdr.pack(fill="x", pady=(20, 4))
        tk.Label(my_hdr, text="My Bookings", font=TITLE, bg=BG, fg=TEXT).pack(side="left")
        btn(my_hdr, "Refresh", self._load_my_tickets, bg="#374151").pack(side="right")

        self.my_frame = tk.Frame(body, bg=SURFACE, padx=10, pady=10,
                                 highlightthickness=1, highlightbackground="#374151")
        self.my_frame.pack(fill="both", expand=True)

        self.my_canvas = tk.Canvas(self.my_frame, bg=SURFACE, highlightthickness=0)
        vsb = tk.Scrollbar(self.my_frame, orient="vertical", command=self.my_canvas.yview)
        self.my_canvas.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        self.my_canvas.pack(side="left", fill="both", expand=True)
        self.my_inner = tk.Frame(self.my_canvas, bg=SURFACE)
        self.my_canvas.create_window((0,0), window=self.my_inner, anchor="nw")
        self.my_inner.bind("<Configure>", lambda e: self.my_canvas.configure(
            scrollregion=self.my_canvas.bbox("all")))

    def _check(self):
        pnr = self.pnr_entry.get().strip()
        if not pnr:
            messagebox.showerror("Error", "Enter a PNR number.")
            return
        row = self.app.booking_service.get_pnr_status(pnr)
        for w in self.result_frame.winfo_children():
            w.destroy()
        self.result_frame.pack(fill="x", pady=12)

        if not row:
            tk.Label(self.result_frame, text="❌  PNR not found.", font=BOLD,
                     bg=SURFACE, fg=RED).pack(pady=12)
            return

        status_color = GREEN if row[12] == "CONFIRMED" else RED
        bdr = GREEN if row[12] == "CONFIRMED" else RED
        self.result_frame.config(highlightbackground=bdr)

        tk.Label(self.result_frame, text=f"PNR: {row[0]}", font=("Segoe UI",14,"bold"),
                 bg=SURFACE, fg=TEXT).pack(anchor="w")
        status_lbl = tk.Label(self.result_frame, text=f"● {row[12]}",
                               font=("Segoe UI",12,"bold"), bg=SURFACE, fg=status_color)
        status_lbl.pack(anchor="w", pady=4)

        info = [
            ("Passenger", f"{row[2]}  (Age: {row[3]})"),
            ("Train", f"{row[5]}  ({row[4]})"),
            ("Route", f"{row[6]} → {row[7]}"),
            ("Date", row[8]),
            ("Class", row[9]),
            ("Seats", str(row[10])),
            ("Total Fare", f"₹{row[11]}"),
            ("Booked at", row[13]),
        ]
        for label, val in info:
            row_f = tk.Frame(self.result_frame, bg=SURFACE)
            row_f.pack(fill="x", pady=2)
            tk.Label(row_f, text=f"{label}:", font=FONT, bg=SURFACE, fg=MUTED, width=14,
                     anchor="w").pack(side="left")
            tk.Label(row_f, text=val, font=BOLD, bg=SURFACE, fg=TEXT).pack(side="left")

    def _load_my_tickets(self):
        for w in self.my_inner.winfo_children():
            w.destroy()
        tickets = self.app.booking_service.get_user_tickets(self.app.current_user["username"])
        if not tickets:
            tk.Label(self.my_inner, text="No bookings yet.", font=FONT,
                     bg=SURFACE, fg=MUTED).pack(pady=10)
            return
        headers = ["PNR","Train","From → To","Date","Class","Seats","Fare","Status"]
        for col, h in enumerate(headers):
            tk.Label(self.my_inner, text=h, font=BOLD, bg="#2d3548", fg=ACCENT,
                     padx=8, pady=4, relief="flat").grid(row=0, column=col, sticky="ew", padx=1, pady=1)
        for r, t in enumerate(tickets, 1):
            bg_row = SURFACE if r%2==0 else "#1e2436"
            status_fg = GREEN if t[12]=="CONFIRMED" else RED
            vals = [t[0], f"{t[5]} ({t[4]})", f"{t[6]} → {t[7]}", t[8], t[9], t[10], f"₹{t[11]}", t[12]]
            for col, val in enumerate(vals):
                fg = status_fg if col==7 else TEXT
                tk.Label(self.my_inner, text=str(val), font=FONT if col!=7 else BOLD,
                         bg=bg_row, fg=fg, padx=8, pady=4).grid(row=r, column=col, sticky="ew", padx=1, pady=1)

    def _back(self):
        self.hide()
        self.app.main_menu.show()

    def show(self):
        self._load_my_tickets()
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()
        self.result_frame.pack_forget()
