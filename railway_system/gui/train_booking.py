import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date, timedelta

BG      = "#1a1f2e"
SURFACE = "#232a3d"
SURFACE2= "#2d3548"
ACCENT  = "#f97316"
TEXT    = "#e8eaf0"
MUTED   = "#9ca3af"
GREEN   = "#22c55e"
FONT    = ("Segoe UI", 10)
BOLD    = ("Segoe UI", 10, "bold")
TITLE   = ("Segoe UI", 15, "bold")
MONO    = ("Courier New", 9)

CLASSES = ["1A","2A","3A","SL","CC","2S","EC"]
CLASS_NAMES = {"1A":"First AC","2A":"Second AC","3A":"Third AC","SL":"Sleeper","CC":"Chair Car","2S":"Second Sitting","EC":"Executive Chair"}

def lbl(parent, text, font=FONT, fg=MUTED, **kw):
    return tk.Label(parent, text=text, font=font, bg=parent["bg"], fg=fg, **kw)

def entry(parent, width=22, **kw):
    return tk.Entry(parent, width=width, bg=SURFACE2, fg=TEXT, insertbackground=TEXT,
                    relief="flat", font=FONT, highlightthickness=1,
                    highlightcolor=ACCENT, highlightbackground="#374151", **kw)

def btn(parent, text, cmd, bg=ACCENT, fg="white", width=None, **kw):
    kw.setdefault("pady", 5)
    b = tk.Button(parent, text=text, command=cmd, bg=bg, fg=fg, font=BOLD, relief="flat",
                  cursor="hand2", activebackground="#ea6c0a", activeforeground="white",
                  **kw)
    if width:
        b.config(width=width)
    return b

class TrainBooking:
    def __init__(self, root, app):
        self.root = root
        self.app  = app
        self.frame = tk.Frame(root, bg=BG)
        self.selected_train = None
        self.found_trains = []
        self._build()

    def _build(self):
        f = self.frame

        # Navbar
        nav = tk.Frame(f, bg=ACCENT, pady=8)
        nav.pack(fill="x")
        btn(nav, "← Back", self._back, bg="#c2540a", pady=3).pack(side="left", padx=12)
        tk.Label(nav, text="🔍  Search & Book Train", font=("Segoe UI", 13, "bold"),
                 bg=ACCENT, fg="white").pack(side="left", padx=10)

        body = tk.Frame(f, bg=BG)
        body.pack(fill="both", expand=True, padx=20, pady=16)

        # ── Search Panel ──
        sp = tk.Frame(body, bg=SURFACE, padx=20, pady=16,
                      highlightthickness=1, highlightbackground="#374151")
        sp.pack(fill="x")

        tk.Label(sp, text="Search Trains", font=TITLE, bg=SURFACE, fg=TEXT).grid(
            row=0, column=0, columnspan=6, sticky="w", pady=(0,12))

        lbl(sp, "From Station").grid(row=1, column=0, sticky="w")
        self.src_var = tk.StringVar()
        self.src_entry = entry(sp, textvariable=self.src_var)
        self.src_entry.grid(row=1, column=1, padx=8, ipady=5)

        lbl(sp, "To Station").grid(row=1, column=2, sticky="w")
        self.dst_var = tk.StringVar()
        self.dst_entry = entry(sp, textvariable=self.dst_var)
        self.dst_entry.grid(row=1, column=3, padx=8, ipady=5)

        lbl(sp, "Travel Date").grid(row=1, column=4, sticky="w")
        self.date_var = tk.StringVar(value=str(date.today() + timedelta(days=1)))
        self.date_entry = entry(sp, width=14, textvariable=self.date_var)
        self.date_entry.grid(row=1, column=5, padx=8, ipady=5)

        btn(sp, "SEARCH TRAINS", self._search).grid(row=2, column=0, columnspan=6, pady=12)

        # Quick routes
        qf = tk.Frame(sp, bg=SURFACE)
        qf.grid(row=3, column=0, columnspan=6, pady=4)
        lbl(qf, "Quick routes: ", fg=MUTED).pack(side="left")
        for (s,d) in [("VISAKHAPATNAM","HYDERABAD"),("HYDERABAD","VISAKHAPATNAM"),
                      ("VISAKHAPATNAM","VIJAYAWADA"),("CHENNAI","KOLKATA"),("MUMBAI","BHUBANESHWAR")]:
            tk.Button(qf, text=f"{s[:4]}→{d[:4]}", font=("Segoe UI",8), bg=SURFACE2, fg=TEXT,
                      relief="flat", cursor="hand2", padx=6, pady=2,
                      command=lambda s=s,d=d: self._quick(s,d)).pack(side="left", padx=3)

        # ── Results ──
        res_frame = tk.Frame(body, bg=BG)
        res_frame.pack(fill="both", expand=True, pady=10)

        self.result_label = tk.Label(res_frame, text="", font=FONT, bg=BG, fg=MUTED)
        self.result_label.pack(anchor="w")

        # Treeview for results
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Custom.Treeview", background=SURFACE, foreground=TEXT,
                        fieldbackground=SURFACE, rowheight=28, font=FONT)
        style.configure("Custom.Treeview.Heading", background=SURFACE2, foreground=ACCENT,
                        font=BOLD, relief="flat")
        style.map("Custom.Treeview", background=[("selected","#374151")])

        cols = ("Code","Train Name","From","To","Departs","Arrives","Hrs","Classes")
        self.tree = ttk.Treeview(res_frame, columns=cols, show="headings",
                                 style="Custom.Treeview", height=8)
        widths = [60,200,130,130,70,70,40,160]
        for col,w in zip(cols,widths):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=w, anchor="center")
        self.tree.pack(fill="x", pady=4)
        self.tree.bind("<<TreeviewSelect>>", self._on_select)

        sb = ttk.Scrollbar(res_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=sb.set)

        # ── Booking Form ──
        self.book_frame = tk.Frame(body, bg=SURFACE, padx=20, pady=16,
                                   highlightthickness=1, highlightbackground=ACCENT)
        self.book_label = tk.Label(self.book_frame, text="", font=TITLE, bg=SURFACE, fg=ACCENT)
        self.book_label.grid(row=0, column=0, columnspan=4, sticky="w", pady=(0,10))

        lbl(self.book_frame, "Passenger Name").grid(row=1, column=0, sticky="w")
        self.pax_name = entry(self.book_frame)
        self.pax_name.grid(row=1, column=1, padx=8, ipady=5)

        lbl(self.book_frame, "Age").grid(row=1, column=2, sticky="w")
        self.pax_age = entry(self.book_frame, width=6)
        self.pax_age.grid(row=1, column=3, padx=8, ipady=5)

        lbl(self.book_frame, "Class").grid(row=2, column=0, sticky="w", pady=8)
        self.class_var = tk.StringVar()
        self.class_combo = ttk.Combobox(self.book_frame, textvariable=self.class_var,
                                        width=20, state="readonly",
                                        font=FONT)
        self.class_combo.grid(row=2, column=1, padx=8, ipady=4)
        self.class_combo.bind("<<ComboboxSelected>>", self._update_fare)

        lbl(self.book_frame, "Seats").grid(row=2, column=2, sticky="w")
        self.seats_var = tk.StringVar(value="1")
        self.seats_spin = tk.Spinbox(self.book_frame, from_=1, to=6, textvariable=self.seats_var,
                                     width=5, bg=SURFACE2, fg=TEXT, font=FONT,
                                     relief="flat", command=self._update_fare)
        self.seats_spin.grid(row=2, column=3, padx=8)

        self.fare_label = tk.Label(self.book_frame, text="", font=BOLD, bg=SURFACE, fg=GREEN)
        self.fare_label.grid(row=3, column=0, columnspan=4, pady=8)

        btn(self.book_frame, "✔  CONFIRM BOOKING", self._book, width=25).grid(
            row=4, column=0, columnspan=4, pady=6)

    def _quick(self, src, dst):
        self.src_var.set(src)
        self.dst_var.set(dst)
        self._search()

    def _search(self):
        src = self.src_var.get().strip().upper()
        dst = self.dst_var.get().strip().upper()
        if not src or not dst:
            messagebox.showerror("Error", "Enter both source and destination.")
            return
        results = self.app.booking_service.search_trains(src, dst)
        self.tree.delete(*self.tree.get_children())
        self.book_frame.pack_forget()
        self.found_trains = results
        if not results:
            self.result_label.config(text=f"No trains found from {src} to {dst}.")
            return
        self.result_label.config(text=f"{len(results)} train(s) found — click a row to select")
        for r in results:
            code,name,src_,dst_,dep,arr,dur = r[0],r[1],r[2],r[3],r[4],r[5],r[6]
            fares = r[7:]
            cls_list = [c for c,f in zip(CLASSES,fares) if f>0]
            self.tree.insert("", "end", values=(code,name,src_,dst_,dep,arr,f"{dur}h",", ".join(cls_list)))

    def _on_select(self, event):
        sel = self.tree.selection()
        if not sel:
            return
        idx = self.tree.index(sel[0])
        self.selected_train = self.found_trains[idx]
        t = self.selected_train
        self.book_label.config(text=f"{t[0]} — {t[1]}  ({t[2]} → {t[3]})")
        # Available classes
        avail = self.app.booking_service.get_available_classes(t[0])
        fares = dict(zip(CLASSES, t[7:]))
        options = [f"{cls}  ({CLASS_NAMES[cls]})  — ₹{fares[cls]}  [{seats} seats]"
                   for cls, seats in avail if fares.get(cls,0)>0]
        self.class_combo["values"] = options
        if options:
            self.class_combo.current(0)
        self._update_fare()
        self.book_frame.pack(fill="x", pady=6)

    def _update_fare(self, event=None):
        if not self.selected_train:
            return
        sel = self.class_var.get()
        if not sel:
            return
        cls = sel.split()[0]
        try:
            seats = int(self.seats_var.get())
        except:
            seats = 1
        fare = self.app.booking_service.get_fare(self.selected_train[0], cls)
        total = fare * seats
        self.fare_label.config(text=f"Total Fare: ₹{total}  ({seats} × ₹{fare})")

    def _book(self):
        if not self.selected_train:
            return
        name = self.pax_name.get().strip()
        age_s = self.pax_age.get().strip()
        sel = self.class_var.get()
        date_str = self.date_var.get().strip()
        if not name or not age_s or not sel:
            messagebox.showerror("Error", "Please fill all fields.")
            return
        try:
            age = int(age_s)
            seats = int(self.seats_var.get())
        except:
            messagebox.showerror("Error", "Invalid age or seats.")
            return
        cls = sel.split()[0]
        ok, result = self.app.booking_service.book_ticket(
            self.app.current_user["username"], name, age,
            self.selected_train[0], date_str, cls, seats)
        if ok:
            messagebox.showinfo("Booking Confirmed! 🎉",
                                f"PNR: {result}\nPassenger: {name}\n"
                                f"Train: {self.selected_train[1]}\nClass: {cls}\n"
                                f"Seats: {seats}\nDate: {date_str}\n\nNote your PNR number!")
            self.book_frame.pack_forget()
            self.selected_train = None
        else:
            messagebox.showerror("Booking Failed", result)

    def _back(self):
        self.hide()
        self.app.main_menu.show()

    def show(self):
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()
        self.book_frame.pack_forget()
