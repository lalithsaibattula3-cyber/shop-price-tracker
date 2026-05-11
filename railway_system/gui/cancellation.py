import tkinter as tk
from tkinter import messagebox

BG      = "#1a1f2e"
SURFACE = "#232a3d"
SURFACE2= "#2d3548"
ACCENT  = "#ef4444"
ORANGE  = "#f97316"
TEXT    = "#e8eaf0"
MUTED   = "#9ca3af"
GREEN   = "#22c55e"
RED     = "#ef4444"
FONT    = ("Segoe UI", 10)
BOLD    = ("Segoe UI", 10, "bold")
TITLE   = ("Segoe UI", 15, "bold")
MONO    = ("Courier New", 11, "bold")

class Cancellation:
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
        tk.Label(nav, text="❌  Cancel Ticket", font=("Segoe UI",13,"bold"),
                 bg=ORANGE, fg="white").pack(side="left", padx=10)

        body = tk.Frame(f, bg=BG)
        body.pack(expand=True, fill="both", padx=30, pady=30)

        # Cancel by PNR
        sp = tk.Frame(body, bg=SURFACE, padx=30, pady=24,
                      highlightthickness=1, highlightbackground="#374151")
        sp.pack(fill="x")

        tk.Label(sp, text="Cancel by PNR", font=TITLE, bg=SURFACE, fg=TEXT).pack(pady=(0,16))

        row = tk.Frame(sp, bg=SURFACE)
        row.pack()
        tk.Label(row, text="PNR Number:", font=FONT, bg=SURFACE, fg=MUTED).pack(side="left", padx=6)
        self.pnr_entry = tk.Entry(row, width=16, bg=SURFACE2, fg=TEXT, insertbackground=TEXT,
                                  font=MONO, relief="flat", highlightthickness=1,
                                  highlightcolor=ACCENT, highlightbackground="#374151")
        self.pnr_entry.pack(side="left", ipady=6, padx=8)
        tk.Button(row, text="CHECK & CANCEL", command=self._check_and_cancel,
                  bg=ACCENT, fg="white", font=BOLD, relief="flat",
                  cursor="hand2", padx=12, pady=5).pack(side="left", padx=8)
        self.pnr_entry.bind("<Return>", lambda e: self._check_and_cancel())

        tk.Label(sp, text="⚠  Cancellation charges may apply as per railway policy.",
                 font=("Segoe UI",9), bg=SURFACE, fg=MUTED).pack(pady=8)

        # Preview card
        self.preview_frame = tk.Frame(body, bg=SURFACE, padx=24, pady=20,
                                      highlightthickness=2, highlightbackground=ACCENT)

        # Active tickets
        active_hdr = tk.Frame(body, bg=BG)
        active_hdr.pack(fill="x", pady=(20, 4))
        tk.Label(active_hdr, text="Your Active Tickets", font=TITLE, bg=BG, fg=TEXT).pack(side="left")
        tk.Button(active_hdr, text="Refresh", command=self._load_active,
                  bg="#374151", fg=TEXT, font=FONT, relief="flat", cursor="hand2",
                  padx=10, pady=3).pack(side="right")

        self.active_frame = tk.Frame(body, bg=SURFACE, padx=10, pady=10,
                                     highlightthickness=1, highlightbackground="#374151")
        self.active_frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.active_frame, bg=SURFACE, highlightthickness=0)
        vsb = tk.Scrollbar(self.active_frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.inner = tk.Frame(self.canvas, bg=SURFACE)
        self.canvas.create_window((0,0), window=self.inner, anchor="nw")
        self.inner.bind("<Configure>", lambda e: self.canvas.configure(
            scrollregion=self.canvas.bbox("all")))

    def _check_and_cancel(self):
        pnr = self.pnr_entry.get().strip()
        if not pnr:
            messagebox.showerror("Error", "Enter a PNR number.")
            return
        row = self.app.booking_service.get_pnr_status(pnr)
        for w in self.preview_frame.winfo_children():
            w.destroy()
        self.preview_frame.pack(fill="x", pady=12)

        if not row:
            tk.Label(self.preview_frame, text="PNR not found.", font=BOLD,
                     bg=SURFACE, fg=RED).pack()
            return
        if row[12] == "CANCELLED":
            tk.Label(self.preview_frame, text="This ticket is already cancelled.", font=BOLD,
                     bg=SURFACE, fg=RED).pack()
            return

        tk.Label(self.preview_frame, text="Ticket Details", font=TITLE, bg=SURFACE, fg=TEXT).pack(anchor="w")
        infos = [("PNR", row[0]),("Passenger", f"{row[2]} (Age {row[3]})"),
                 ("Train", f"{row[5]} ({row[4]})"),("Route", f"{row[6]} → {row[7]}"),
                 ("Date", row[8]),("Class", row[9]),("Seats", str(row[10])),("Fare", f"₹{row[11]}")]
        for label, val in infos:
            rf = tk.Frame(self.preview_frame, bg=SURFACE)
            rf.pack(fill="x", pady=1)
            tk.Label(rf, text=f"{label}:", font=FONT, bg=SURFACE, fg=MUTED, width=12, anchor="w").pack(side="left")
            tk.Label(rf, text=val, font=BOLD, bg=SURFACE, fg=TEXT).pack(side="left")

        refund = int(row[11] * 0.75)
        tk.Label(self.preview_frame, text=f"Estimated Refund: ₹{refund}  (75% of ₹{row[11]})",
                 font=BOLD, bg=SURFACE, fg=GREEN).pack(pady=8)

        tk.Button(self.preview_frame, text="✔  CONFIRM CANCELLATION",
                  command=lambda pnr=row[0]: self._do_cancel(pnr),
                  bg=RED, fg="white", font=BOLD, relief="flat",
                  cursor="hand2", padx=16, pady=6).pack()

    def _do_cancel(self, pnr):
        if not messagebox.askyesno("Confirm Cancellation",
                                   f"Are you sure you want to cancel PNR {pnr}?\nThis cannot be undone."):
            return
        ok, msg = self.app.booking_service.cancel_ticket(pnr, self.app.current_user["username"])
        if ok:
            messagebox.showinfo("Cancelled", msg)
            self.preview_frame.pack_forget()
            self.pnr_entry.delete(0,"end")
            self._load_active()
        else:
            messagebox.showerror("Error", msg)

    def _load_active(self):
        for w in self.inner.winfo_children():
            w.destroy()
        tickets = [t for t in self.app.booking_service.get_user_tickets(
            self.app.current_user["username"]) if t[12]=="CONFIRMED"]
        if not tickets:
            tk.Label(self.inner, text="No active tickets.", font=FONT, bg=SURFACE, fg=MUTED).pack(pady=10)
            return
        headers = ["PNR","Train","From → To","Date","Class","Seats","Fare","Action"]
        for col, h in enumerate(headers):
            tk.Label(self.inner, text=h, font=BOLD, bg="#2d3548", fg=ACCENT,
                     padx=8, pady=4).grid(row=0, column=col, sticky="ew", padx=1, pady=1)
        for r, t in enumerate(tickets, 1):
            bg_row = SURFACE if r%2==0 else "#1e2436"
            vals = [t[0], f"{t[5]}", f"{t[6]} → {t[7]}", t[8], t[9], t[10], f"₹{t[11]}"]
            for col, val in enumerate(vals):
                tk.Label(self.inner, text=str(val), font=FONT, bg=bg_row, fg=TEXT,
                         padx=8, pady=4).grid(row=r, column=col, sticky="ew", padx=1, pady=1)
            tk.Button(self.inner, text="Cancel", font=FONT, bg=RED, fg="white",
                      relief="flat", cursor="hand2", padx=8, pady=2,
                      command=lambda pnr=t[0]: self._quick_cancel(pnr)).grid(
                          row=r, column=7, padx=4, pady=2)

    def _quick_cancel(self, pnr):
        self.pnr_entry.delete(0,"end")
        self.pnr_entry.insert(0, pnr)
        self._check_and_cancel()

    def _back(self):
        self.hide()
        self.app.main_menu.show()

    def show(self):
        self._load_active()
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()
        self.preview_frame.pack_forget()
