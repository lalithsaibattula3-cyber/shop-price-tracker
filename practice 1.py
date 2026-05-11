# a = "hello python "

# result = ""
# for ch in a:
#     if  ch not in result:
#         result += ch
# print(result)

# words = a.split()
# longest = ""
# for word in words:
#     if len(word) > len (longest):
#         longest = word
# print(longest)
# print(len(longest))


# #string compression 
# b = input("enter a string: ")
# compressed = ""
# count = 1
# for i in range (len(b)-1):
#     if b[i] == b[i+1]:
#         count += 1
#     else :
#         compressed += b[i] + str(count)
#         count = 1
#         compressed += b[-1] + str(count)
# print(compressed)
##
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict["year"])
# a = "hello"
# print(str.upper(a))
# txt = "Hello, welcodme to my world."
# print(txt.find("z"))
# print(txt.index("z"))

# a = input("enter a string: ")
# rev = a[::-1]
# print(rev)

# a =input("enter a string: ")
# rev = a[::-1]
# if(rev == a ):
#     print("palindrome")
# else:
#     print("not palindrome")

# a = input("enter a string: ")
# print(len(a))

# b = input("enter a string:")
# count = 0
# for ch in b:
#     if ch.lower()in "aeiou":
#         count += 1
# print(count)

# s = input("enter a string: ")
# b = s.replace(" ","")
# print(b)

# a = 5
# for i in range(0 , a):
#     for j in range (0,a+1):
#         print(a)
#     print("")



import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np
import os
import random
import string

from captcha.image import ImageCaptcha   # pip install captcha
from PIL import Image, ImageTk          # pip install pillow


class SmartRailwaySystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Smart Railway Reservation System")
        self.root.geometry("900x700")
        self.root.configure(bg="#2c3e50")

        self.files = {
            "users": "users.xlsx",
            "trains": "trains.xlsx",
            "tickets": "tickets.xlsx",
        }
        self.current_user = None

        self.captcha_text = ""      # current captcha value
        self.captcha_image_label = None
        self.captcha_entry = None

        self.init_files()
        self.show_login()

    # ---------- Excel helpers ----------

    def clean_df(self, df):
        """Remove empty rows and NaN in Username column."""
        df = df.replace("", np.nan)
        df = df.dropna(subset=["Username"])
        return df

    def init_files(self):
        """Create base Excel files if they don't exist."""
        if not os.path.exists(self.files["users"]):
            pd.DataFrame(
                {
                    "Username": ["admin", "surya"],
                    "Password": ["1234", "1234"],
                }
            ).to_excel(self.files["users"], index=False)

        if not os.path.exists(self.files["trains"]):
            pd.DataFrame(
                {
                    "Train_Code": ["T101", "T102"],
                    "Name": ["Rajdhani Express", "Shatabdi Express"],
                    "1A": [24, 0],
                    "2A": [72, 0],
                    "3A": [108, 0],
                    "SL": [200, 0],
                    "CC": [90, 78],
                }
            ).to_excel(self.files["trains"], index=False)

        if not os.path.exists(self.files["tickets"]):
            pd.DataFrame(
                columns=[
                    "PNR",
                    "Username",
                    "Name",
                    "Train",
                    "Class",
                    "Seats",
                    "Fare",
                    "Status",
                ]
            ).to_excel(self.files["tickets"], index=False)

    # ---------- CAPTCHA helpers ----------

    def generate_captcha_text(self, length: int = 6) -> str:
        chars = string.ascii_uppercase + string.digits
        return "".join(random.choice(chars) for _ in range(length))

    def refresh_captcha(self):
        """Generate new captcha text + image and display it."""
        self.captcha_text = self.generate_captcha_text()

        generator = ImageCaptcha(width=220, height=70)
        img_data = generator.generate(self.captcha_text)
        image = Image.open(img_data)
        photo = ImageTk.PhotoImage(image)

        # update label
        self.captcha_image_label.config(image=photo)
        self.captcha_image_label.image = photo  # keep reference

        # clear entry
        if self.captcha_entry is not None:
            self.captcha_entry.delete(0, tk.END)

    # ---------- UI screens ----------

    def show_login(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        login_frame = tk.Frame(self.root, bg="#34495e", padx=100, pady=80)
        login_frame.pack(expand=True)

        title = tk.Label(
            login_frame,
            text="🚂 Smart Railway System",
            font=("Arial", 26, "bold"),
            fg="#ecf0f1",
            bg="#34495e",
        )
        title.pack(pady=20)

        # Username
        tk.Label(
            login_frame,
            text="Username:",
            font=("Arial", 14),
            fg="white",
            bg="#34495e",
        ).pack(pady=(15, 5))
        self.username_entry = tk.Entry(
            login_frame, font=("Arial", 14), width=25, justify="center"
        )
        self.username_entry.pack(pady=5)
        self.username_entry.focus()

        # Password
        tk.Label(
            login_frame,
            text="Password:",
            font=("Arial", 14),
            fg="white",
            bg="#34495e",
        ).pack(pady=(10, 5))
        self.password_entry = tk.Entry(
            login_frame, font=("Arial", 14), width=25, show="*", justify="center"
        )
        self.password_entry.pack(pady=5)

        # CAPTCHA area
        captcha_frame = tk.Frame(login_frame, bg="#34495e")
        captcha_frame.pack(pady=20)

        tk.Label(
            captcha_frame,
            text="Enter CAPTCHA:",
            font=("Arial", 14, "bold"),
            fg="#f1c40f",
            bg="#34495e",
        ).pack(pady=(0, 5))

        self.captcha_image_label = tk.Label(captcha_frame, bg="white")
        self.captcha_image_label.pack(pady=5)

        # generate first captcha
        self.refresh_captcha()

        entry_frame = tk.Frame(captcha_frame, bg="#34495e")
        entry_frame.pack(pady=5)

        self.captcha_entry = tk.Entry(entry_frame, font=("Arial", 14), width=10)
        self.captcha_entry.pack(side=tk.LEFT, padx=5)

        tk.Button(
            entry_frame,
            text="🔄 Refresh",
            command=self.refresh_captcha,
            bg="#95a5a6",
            fg="white",
            font=("Arial", 10, "bold"),
        ).pack(side=tk.LEFT, padx=5)

        # Buttons
        btn_frame = tk.Frame(login_frame, bg="#34495e")
        btn_frame.pack(pady=25)

        tk.Button(
            btn_frame,
            text="🔐 Login",
            command=self.login,
            bg="#3498db",
            fg="white",
            font=("Arial", 14, "bold"),
            padx=40,
            pady=10,
            cursor="hand2",
        ).pack(side=tk.LEFT, padx=15)

        tk.Button(
            btn_frame,
            text="➕ Register",
            command=self.show_register,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 14, "bold"),
            padx=40,
            pady=10,
            cursor="hand2",
        ).pack(side=tk.LEFT, padx=15)

    def show_register(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        reg_frame = tk.Frame(self.root, bg="#34495e", padx=100, pady=100)
        reg_frame.pack(expand=True)

        tk.Label(
            reg_frame,
            text="👤 New User Registration",
            font=("Arial", 22, "bold"),
            fg="#ecf0f1",
            bg="#34495e",
        ).pack(pady=20)

        tk.Label(
            reg_frame,
            text="New Username:",
            font=("Arial", 14),
            fg="white",
            bg="#34495e",
        ).pack(pady=(20, 5))
        self.reg_username = tk.Entry(reg_frame, font=("Arial", 14), width=25)
        self.reg_username.pack(pady=5)
        self.reg_username.focus()

        tk.Label(
            reg_frame,
            text="New Password:",
            font=("Arial", 14),
            fg="white",
            bg="#34495e",
        ).pack(pady=(10, 5))
        self.reg_password = tk.Entry(
            reg_frame, font=("Arial", 14), width=25, show="*"
        )
        self.reg_password.pack(pady=5)

        tk.Button(
            reg_frame,
            text="✅ Register",
            command=self.register_user,
            bg="#27ae60",
            fg="white",
            font=("Arial", 16, "bold"),
            padx=50,
            pady=12,
            cursor="hand2",
        ).pack(pady=25)

        tk.Button(
            reg_frame,
            text="← Back to Login",
            command=self.show_login,
            bg="#95a5a6",
            fg="white",
            font=("Arial", 12),
        ).pack()

    # ---------- Auth logic ----------

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        captcha_input = self.captcha_entry.get().strip().upper()

        # 1) CAPTCHA check
        if captcha_input != self.captcha_text:
            messagebox.showerror("CAPTCHA Error", "Incorrect CAPTCHA, try again.")
            self.refresh_captcha()
            return

        # 2) Username/password check
        try:
            df = pd.read_excel(self.files["users"])
            df = self.clean_df(df)

            match = df[
                (df["Username"].astype(str) == username)
                & (df["Password"].astype(str) == password)
            ]

            if not match.empty:
                self.current_user = username
                messagebox.showinfo("Success", f"Welcome {username}!")
                self.show_main_menu()
            else:
                messagebox.showerror("Login Failed", "Invalid username/password.")
                self.username_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
                self.refresh_captcha()

        except Exception as e:
            messagebox.showerror("Error", f"Login error:\n{e}")

    def register_user(self):
        username = self.reg_username.get().strip()
        password = self.reg_password.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "Please fill both fields.")
            return

        try:
            df = pd.read_excel(self.files["users"])
            df = self.clean_df(df)

            if username in df["Username"].astype(str).values:
                messagebox.showerror("Error", "Username already exists.")
                return

            new_df = pd.DataFrame({"Username": [username], "Password": [password]})
            df = pd.concat([df, new_df], ignore_index=True)
            df.to_excel(self.files["users"], index=False)

            messagebox.showinfo("Success", "Registered successfully. Please login.")
            self.show_login()

        except PermissionError:
            messagebox.showerror("Error", "Close users.xlsx and try again.")
        except Exception as e:
            messagebox.showerror("Error", f"Registration error:\n{e}")

    # ---------- Main menu & feature stubs ----------

    def show_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        header_frame = tk.Frame(self.root, bg="#2c3e50", pady=20)
        header_frame.pack(fill="x")
        tk.Label(
            header_frame,
            text=f"👋 Welcome {self.current_user}",
            font=("Arial", 18, "bold"),
            fg="white",
            bg="#2c3e50",
        ).pack()

        btn_frame = tk.Frame(self.root, bg="#2c3e50", padx=100, pady=40)
        btn_frame.pack(expand=True)

        buttons = [
            ("🚂 View Trains", self.view_trains, "#3498db"),
            ("🎫 Book Ticket", self.book_ticket, "#27ae60"),
            ("🔍 PNR Status", self.pnr_status, "#f39c12"),
            ("❌ Cancel Ticket", self.cancel_ticket, "#e74c3c"),
            ("📊 Reports", self.show_reports, "#9b59b6"),
        ]

        for text, command, color in buttons:
            tk.Button(
                btn_frame,
                text=text,
                command=command,
                bg=color,
                fg="white",
                font=("Arial", 16, "bold"),
                width=25,
                height=2,
                cursor="hand2",
            ).pack(pady=12)

        tk.Button(
            btn_frame,
            text="🚪 Logout",
            command=self.show_login,
            bg="#95a5a6",
            fg="white",
            font=("Arial", 14, "bold"),
            width=25,
            height=2,
        ).pack(pady=20)

    # For now these just show messages – you can fill in Excel logic later

    def view_trains(self):
        try:
            df = pd.read_excel(self.files["trains"])
            messagebox.showinfo("Trains", f"{len(df)} trains loaded from Excel.")
        except Exception as e:
            messagebox.showerror("Error", f"Cannot read trains.xlsx:\n{e}")

    def book_ticket(self):
        messagebox.showinfo("Info", "Ticket booking UI will be added here.")

    def pnr_status(self):
        messagebox.showinfo("Info", "PNR status UI will be added here.")

    def cancel_ticket(self):
        messagebox.showinfo("Info", "Cancellation UI will be added here.")

    def show_reports(self):
        try:
            df = pd.read_excel(self.files["tickets"])
            messagebox.showinfo(
                "Reports",
                f"Total tickets: {len(df)}\nTotal revenue: ₹{df['Fare'].sum() if 'Fare' in df.columns else 0}",
            )
        except Exception as e:
            messagebox.showerror("Error", f"Cannot read tickets.xlsx:\n{e}")

    # ---------- Run ----------

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = SmartRailwaySystem()
    app.run()
