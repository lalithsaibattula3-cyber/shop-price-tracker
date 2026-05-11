import tkinter as tk
from db.connection import DBConnection
from db.users_db import init_users_db
from db.trains_db import init_trains_db
from db.tickets_db import init_tickets_db
from services.auth_service import AuthService
from services.booking_service import BookingService
from services.report_service import ReportService
from gui.login_screen import LoginScreen
from gui.main_menu import MainMenu
from gui.train_booking import TrainBooking
from gui.pnr_status import PNRStatus
from gui.cancellation import Cancellation
from gui.reports import Reports
from gui.admin_panel import AdminPanel


class SmartRailwaySystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("***Smart Railway Reservation System***")
        self.root.geometry("1000x720")
        self.root.minsize(900, 650)
        self.root.configure(bg="#0e0808")

        # Try to set window icon (ignore if unavailable)
        try:
            self.root.iconbitmap(default="")
        except:
            pass

        self.db_conn = DBConnection()
        self.files = self.db_conn.files
        self.current_user = None

        # Init all databases
        init_users_db(self.files["users"])
        init_trains_db(self.files["trains"])
        init_tickets_db(self.files["tickets"])

        # Services
        self.auth_service    = AuthService(self.files["users"])
        self.booking_service = BookingService(self.files["tickets"], self.files["trains"])
        self.report_service  = ReportService(self.files["tickets"])

        # GUI screens
        self.login_screen  = LoginScreen(self.root, self)
        self.main_menu     = MainMenu(self.root, self)
        self.train_booking = TrainBooking(self.root, self)
        self.pnr_status    = PNRStatus(self.root, self)
        self.cancellation  = Cancellation(self.root, self)
        self.reports       = Reports(self.root, self)
        self.admin_panel   = AdminPanel(self.root, self)

        self.login_screen.show_login()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = SmartRailwaySystem()
    app.run()
