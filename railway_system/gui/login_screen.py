import tkinter as tk
from tkinter import messagebox, ttk
from captcha.image import ImageCaptcha
from PIL import Image, ImageTk
import random
import string
BG      = "#1a1f2e"
SURFACE = "#232a3d"
ACCENT  = "#f97316"
TEXT    = "#e8eaf0"
MUTED   = "#9ca3af"
GREEN   = "#22c55e"
RED     = "#ef4444"
FONT    = ("Segoe UI", 10)
BOLD    = ("Segoe UI", 10, "bold")
TITLE   = ("Segoe UI", 22, "bold")
SUB     = ("Segoe UI", 11)

def styled_entry(parent, show=None, width=30):
    e = tk.Entry(parent, show=show, width=width, bg=SURFACE, fg=TEXT,
                 insertbackground=TEXT, relief="flat", font=FONT,
                 highlightthickness=1, highlightcolor=ACCENT, highlightbackground="#374151")
    return e

def styled_button(parent, text, command, bg=ACCENT, fg="white", width=20):
    b = tk.Button(parent, text=text, command=command, bg=bg, fg=fg,
                  font=BOLD, relief="flat", cursor="hand2", width=width,
                  activebackground="#ea6c0a", activeforeground="white", pady=6)
    return b

class LoginScreen:
    def __init__(self, root, app):
        self.root = root
        self.app  = app
        self.frame = tk.Frame(root, bg=BG)
        self._build()

    def _build(self):
        f = self.frame
        # Header strip
        hdr = tk.Frame(f, bg=ACCENT, height=6)
        hdr.pack(fill="x")

        center = tk.Frame(f, bg=BG)
        center.pack(expand=True)

        # Logo area
        logo_f = tk.Frame(center, bg=BG)
        logo_f.pack(pady=(40, 10))
        tk.Label(logo_f, text="🚆", font=("Segoe UI", 48), bg=BG, fg=ACCENT).pack()
        tk.Label(logo_f, text="Smart Railway Reservation", font=TITLE, bg=BG, fg=TEXT).pack()
        

        # Card
        card = tk.Frame(center, bg=SURFACE, padx=40, pady=30,
                        highlightthickness=1, highlightbackground="#374151")
        card.pack(pady=20, ipadx=10)

        self.tab_var = tk.StringVar(value="login")
        tab_f = tk.Frame(card, bg=SURFACE)
        tab_f.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        self.btn_login_tab = tk.Button(tab_f, text="Login", font=BOLD, bg=ACCENT, fg="white",
                                       relief="flat", padx=20, pady=4, cursor="hand2",
                                       command=self._show_login_tab)
        self.btn_login_tab.pack(side="left", padx=2)
        self.btn_reg_tab = tk.Button(tab_f, text="Register", font=BOLD, bg="#374151", fg=TEXT,
                                     relief="flat", padx=20, pady=4, cursor="hand2",
                                     command=self._show_reg_tab)
        self.btn_reg_tab.pack(side="left", padx=2)

        # Login fields
        self.login_frame = tk.Frame(card, bg=SURFACE)
        self._build_login(self.login_frame)
        self.login_frame.grid(row=1, column=0, columnspan=2)

        # Register fields
        self.reg_frame = tk.Frame(card, bg=SURFACE)
        self._build_register(self.reg_frame)

       
    def _build_login(self, f):
        tk.Label(f, text="Username", font=FONT, bg=SURFACE, fg=MUTED).grid(row=0, column=0, sticky="w", pady=4)
        self.login_user = styled_entry(f)
        self.login_user.grid(row=1, column=0, pady=(0,10), ipady=6, padx=4)

        tk.Label(f, text="Password", font=FONT, bg=SURFACE, fg=MUTED).grid(row=2, column=0, sticky="w", pady=4)
        self.login_pw = styled_entry(f, show="•")
        self.login_pw.grid(row=3, column=0, pady=(0,10), ipady=6, padx=4)

        captcha_frame = tk.Frame(f, bg=SURFACE)
        captcha_frame.grid(row=4, column=0, pady=(0,14), sticky="w")

        tk.Label(captcha_frame, text="Enter CAPTCHA", font=FONT, bg=SURFACE, fg=MUTED).pack(anchor="w", pady=(0,4))

        image_frame = tk.Frame(captcha_frame, bg=SURFACE)
        image_frame.pack(pady=(0,8), anchor="w")

        self.captcha_image_label = tk.Label(image_frame, bg="white", bd=1, relief="solid")
        self.captcha_image_label.pack(side="left")

        tk.Button(image_frame, text="⟳", command=self._refresh_captcha,
                  bg="#69778B", fg="white", font=("Segoe UI", 14), relief="flat",
                  cursor="hand2", padx=10, pady=8).pack(side="left", padx=(8, 0))

        self.captcha_entry = styled_entry(captcha_frame, width=20)
        self.captcha_entry.pack(pady=(0,50), ipady=6, padx=4, anchor="center")

        styled_button(f, "LOGIN", self._do_login).grid(row=5, column=0, pady=4)
        self.login_user.bind("<Return>", lambda e: self._do_login())
        self.login_pw.bind("<Return>", lambda e: self._do_login())
        self.captcha_entry.bind("<Return>", lambda e: self._do_login())
        self._refresh_captcha()

    def _build_register(self, f):
        tk.Label(f, text="Username", font=FONT, bg=SURFACE, fg=MUTED).grid(row=0, column=0, sticky="w", pady=4)
        self.reg_user = styled_entry(f)
        self.reg_user.grid(row=1, column=0, pady=(0,10), ipady=6, padx=4)

        tk.Label(f, text="Password", font=FONT, bg=SURFACE, fg=MUTED).grid(row=2, column=0, sticky="w", pady=4)
        self.reg_pw = styled_entry(f, show="•")
        self.reg_pw.grid(row=3, column=0, pady=(0,10), ipady=6, padx=4)

        tk.Label(f, text="Confirm Password", font=FONT, bg=SURFACE, fg=MUTED).grid(row=4, column=0, sticky="w", pady=4)
        self.reg_pw2 = styled_entry(f, show="•")
        self.reg_pw2.grid(row=5, column=0, pady=(0,16), ipady=6, padx=4)

        styled_button(f, "REGISTER", self._do_register).grid(row=6, column=0, pady=4)

    def _show_login_tab(self):
        self.reg_frame.grid_forget()
        self.login_frame.grid(row=1, column=0, columnspan=2)
        self.btn_login_tab.config(bg=ACCENT)
        self.btn_reg_tab.config(bg="#374151")

    def _show_reg_tab(self):
        self.login_frame.grid_forget()
        self.reg_frame.grid(row=1, column=0, columnspan=2)
        self.btn_reg_tab.config(bg=ACCENT)
        self.btn_login_tab.config(bg="#374151")

    def _do_login(self):
        u = self.login_user.get().strip()
        p = self.login_pw.get().strip()
        captcha_value = self.captcha_entry.get().strip().upper()

        if not u or not p:
            messagebox.showerror("Error", "Please enter username and password.")
            return
        if not captcha_value:
            messagebox.showerror("CAPTCHA Error", "Please enter the CAPTCHA text.")
            return
        if captcha_value != self.captcha_text:
            messagebox.showerror("CAPTCHA Error", "Incorrect CAPTCHA, please try again.")
            self._refresh_captcha()
            return

        user = self.app.auth_service.login(u, p)
        if user:
            self.app.current_user = user
            self.login_pw.delete(0, "end")
            self.login_user.delete(0, "end")
            self.captcha_entry.delete(0, "end")
            self.hide()
            self.app.main_menu.show()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
            self._refresh_captcha()

    def _generate_captcha_text(self, length=6):
        chars = string.ascii_uppercase + string.digits
        return "".join(random.choice(chars) for _ in range(length))

    def _refresh_captcha(self):
        self.captcha_text = self._generate_captcha_text()
        generator = ImageCaptcha(width=220, height=70)
        img_data = generator.generate(self.captcha_text)
        image = Image.open(img_data)
        photo = ImageTk.PhotoImage(image)

        self.captcha_image_label.config(image=photo)
        self.captcha_image_label.image = photo

        if hasattr(self, "captcha_entry") and self.captcha_entry is not None:
            self.captcha_entry.delete(0, "end")

    def _do_register(self):
        u = self.reg_user.get().strip()
        p = self.reg_pw.get().strip()
        p2 = self.reg_pw2.get().strip()
        if not u or not p:
            messagebox.showerror("Error", "All fields required.")
            return
        if p != p2:
            messagebox.showerror("Error", "Passwords do not match.")
            return
        ok, msg = self.app.auth_service.register(u, p)
        if ok:
            messagebox.showinfo("Success", msg)
            self._show_login_tab()
        else:
            messagebox.showerror("Error", msg)

    def show_login(self):
        self.frame.pack(fill="both", expand=True)

    def show(self):
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()
