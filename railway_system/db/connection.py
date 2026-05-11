import os

class DBConnection:
    def __init__(self, base_dir=None):
        if base_dir is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.files = {
            "users":   os.path.join(base_dir, "data", "users.db"),
            "trains":  os.path.join(base_dir, "data", "trains.db"),
            "tickets": os.path.join(base_dir, "data", "tickets.db"),
        }
        os.makedirs(os.path.join(base_dir, "data"), exist_ok=True)
