import tkinter as tk
from tkinter import ttk, messagebox

BG      = "#1a1f2e"
SURFACE = "#232a3d"
SURFACE2= "#2d3548"
ACCENT  = "#f97316"
TEXT    = "#e8eaf0"
MUTED   = "#9ca3af"
GREEN   = "#22c55e"
RED     = "#ef4444"
BLUE    = "#3b82f6"
FONT    = ("Segoe UI", 10)
BOLD    = ("Segoe UI", 10, "bold")
TITLE   = ("Segoe UI", 15, "bold")

class AdminPanel:
    def __init__(self, root, app):
        self.root = root
        self.app  = app
        self.frame = tk.Frame(root, bg=BG)
        self._build()

    def _build(self):
        f = self.frame

        nav = tk.Frame(f, bg="#7c3aed", pady=8)
        nav.pack(fill="x")
        tk.Button(nav, text="← Back", command=self._back, bg="#5b21b6", fg="white",
                  font=BOLD, relief="flat", cursor="hand2", padx=12, pady=3).pack(side="left", padx=12)
        tk.Label(nav, text="⚙  Admin Panel", font=("Segoe UI",13,"bold"),
                 bg="#7c3aed", fg="white").pack(side="left", padx=10)
        tk.Button(nav, text="↻ Refresh", command=self._load, bg="#5b21b6", fg=TEXT,
                  font=FONT, relief="flat", cursor="hand2", padx=12, pady=3).pack(side="right", padx=12)

        # Tabs
        nb = ttk.Notebook(f)
        style = ttk.Style()
        style.configure("TNotebook", background=BG, borderwidth=0)
        style.configure("TNotebook.Tab", background=SURFACE2, foreground=TEXT,
                        font=BOLD, padding=[16, 8])
        style.map("TNotebook.Tab", background=[("selected","#7c3aed")], foreground=[("selected","white")])
        nb.pack(fill="both", expand=True, padx=10, pady=10)

        # ── Tab 1: All Tickets ──
        tickets_tab = tk.Frame(nb, bg=BG)
        nb.add(tickets_tab, text="  All Tickets  ")
        self._build_tickets_tab(tickets_tab)

        # ── Tab 2: Users ──
        users_tab = tk.Frame(nb, bg=BG)
        nb.add(users_tab, text="  Users  ")
        self._build_users_tab(users_tab)

        # ── Tab 3: Trains ──
        trains_tab = tk.Frame(nb, bg=BG)
        nb.add(trains_tab, text="  Trains DB  ")
        self._build_trains_tab(trains_tab)

    def _build_tickets_tab(self, parent):
        style = ttk.Style()
        style.configure("Adm.Treeview", background=SURFACE, foreground=TEXT,
                        fieldbackground=SURFACE, rowheight=26, font=FONT)
        style.configure("Adm.Treeview.Heading", background=SURFACE2, foreground=ACCENT, font=BOLD)
        style.map("Adm.Treeview", background=[("selected","#374151")])

        cols = ("PNR","User","Passenger","Train","From","To","Date","Cls","Seats","Fare","Status")
        self.tickets_tree = ttk.Treeview(parent, columns=cols, show="headings",
                                         style="Adm.Treeview", height=20)
        widths = [100,80,110,160,110,110,85,45,50,70,90]
        for col,w in zip(cols,widths):
            self.tickets_tree.heading(col, text=col)
            self.tickets_tree.column(col, width=w, anchor="center")
        vsb = ttk.Scrollbar(parent, orient="vertical", command=self.tickets_tree.yview)
        hsb = ttk.Scrollbar(parent, orient="horizontal", command=self.tickets_tree.xview)
        self.tickets_tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.pack(side="right", fill="y")
        hsb.pack(side="bottom", fill="x")
        self.tickets_tree.pack(fill="both", expand=True)

    def _build_users_tab(self, parent):
        style = ttk.Style()
        cols = ("ID","Username","Role")
        self.users_tree = ttk.Treeview(parent, columns=cols, show="headings",
                                       style="Adm.Treeview", height=15)
        for col in cols:
            self.users_tree.heading(col, text=col)
            self.users_tree.column(col, width=200, anchor="center")
        self.users_tree.pack(fill="both", expand=True, padx=10, pady=10)

    def _build_trains_tab(self, parent):
        cols = ("Code","Name","From","To","Dep","Arr","Hrs","1A","2A","3A","SL","CC","2S","EC")
        self.trains_tree = ttk.Treeview(parent, columns=cols, show="headings",
                                        style="Adm.Treeview", height=20)
        widths = [60,180,120,120,60,60,40,50,50,50,50,50,50,50]
        for col,w in zip(cols,widths):
            self.trains_tree.heading(col, text=col)
            self.trains_tree.column(col, width=w, anchor="center")
        vsb = ttk.Scrollbar(parent, orient="vertical", command=self.trains_tree.yview)
        hsb = ttk.Scrollbar(parent, orient="horizontal", command=self.trains_tree.xview)
        self.trains_tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.pack(side="right", fill="y")
        hsb.pack(side="bottom", fill="x")
        self.trains_tree.pack(fill="both", expand=True)

    def _load(self):
        # Tickets
        self.tickets_tree.delete(*self.tickets_tree.get_children())
        for t in self.app.booking_service.get_all_tickets():
            clr = "" if t[12]=="CONFIRMED" else "cancelled"
            self.tickets_tree.insert("", "end", values=(
                t[0],t[1],t[2],t[5],t[6],t[7],t[8],t[9],t[10],f"₹{t[11]}",t[12]), tags=(clr,))
        self.tickets_tree.tag_configure("cancelled", foreground=RED)

        # Users
        self.users_tree.delete(*self.users_tree.get_children())
        for u in self.app.auth_service.get_all_users():
            self.users_tree.insert("", "end", values=u)

        # Trains
        import sqlite3
        self.trains_tree.delete(*self.trains_tree.get_children())
        conn = sqlite3.connect(self.app.files["trains"])
        c = conn.cursor()
        c.execute("SELECT * FROM trains ORDER BY train_code")
        for row in c.fetchall():
            fares = [str(f) if f>0 else "—" for f in row[8:]]
            self.trains_tree.insert("", "end", values=(row[0],row[1],row[2],row[3],row[4],row[5],row[7])+tuple(fares))
        conn.close()

    def _back(self):
        self.hide()
        self.app.main_menu.show()

    def show(self):
        self._load()
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()
