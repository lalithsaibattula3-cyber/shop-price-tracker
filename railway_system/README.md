# Smart Railway Reservation System

A fully working Python + Tkinter + SQLite desktop application for train ticket booking.

## Features
- **Login / Register** — user accounts stored in SQLite
- **Search Trains** — search by source & destination from 30 real AP/Telangana/Pan-India trains
- **Book Ticket** — select class, seats, passenger details; generates unique PNR
- **PNR Status** — look up any booking by PNR number
- **Cancel Ticket** — cancel with 75% refund estimate; seats restored automatically
- **Reports** — summary cards + train-wise booking analytics
- **Admin Panel** — view all tickets, users, and full train database (login: admin / admin123)

## Project Structure
```
railway_system/
├── main.py                   ← Entry point (run this)
├── data/                     ← SQLite DB files (auto-created on first run)
│   ├── users.db
│   ├── trains.db
│   └── tickets.db
├── db/
│   ├── connection.py
│   ├── users_db.py
│   ├── trains_db.py          ← All 30 trains pre-loaded
│   └── tickets_db.py
├── services/
│   ├── auth_service.py
│   ├── booking_service.py
│   └── report_service.py
└── gui/
    ├── login_screen.py
    ├── main_menu.py
    ├── train_booking.py
    ├── pnr_status.py
    ├── cancellation.py
    ├── reports.py
    └── admin_panel.py
```

## Requirements
- Python 3.8+
- tkinter (usually bundled with Python)
- sqlite3 (standard library)

No pip installs needed — all standard library!

## How to Run
```bash
cd railway_system
python main.py
```

## Default Login
| Username | Password  | Role  |
|----------|-----------|-------|
| admin    | admin123  | admin |

You can register new user accounts from the login screen.

## Trains Included (30 trains)
- Ratnachal Express (12717/12718) — VSKP ↔ BZA
- Godavari Express (12727/12728) — VSKP ↔ HYD
- Prashanthi Express (18463/18464) — BBS ↔ SBC
- Vande Bharat Express (multiple) — SC↔VSKP, SC↔TPTY, VBZ↔NRP, etc.
- Janmabhoomi Express (12805/12806) — VSKP ↔ SC
- Konark Express (11019/11020) — CSMT ↔ BBS
- Visakha Express (17015/17016) — BBS ↔ SC
- Tirumula Express (18521/18522) — VSKP ↔ HX
- East Coast Express (18045/18046) — KOLKATA ↔ SC
- Coromandel Express (12841/12842) — MAS ↔ KOLKATA
- Puri-Tirupathi Express (17479/17480)
- Mumbai LLT / Visakhapatnam Express (18519/18520)

## Classes Available
| Code | Name             |
|------|-----------------|
| 1A   | First AC        |
| 2A   | Second AC       |
| 3A   | Third AC        |
| SL   | Sleeper         |
| CC   | Chair Car       |
| 2S   | Second Sitting  |
| EC   | Executive Chair |
