"""
Q20. Smart Parking System
Track vehicles entering and exiting, available slots, and display status messages.
"""


def smart_parking_system(total_slots):
    parked = 0
    while True:
        print(f"Available slots: {total_slots - parked}")
        action = input("Enter 'in' for entry, 'out' for exit, or 'exit' to stop: ").strip().lower()
        if action == "exit":
            print("Ending parking simulation.")
            break
        if action == "in":
            if parked >= total_slots:
                print("Parking Full")
            else:
                parked += 1
                print("Vehicle entered.")
        elif action == "out":
            if parked <= 0:
                print("No vehicles to exit.")
            else:
                parked -= 1
                print("Vehicle exited.")
        else:
            print("Invalid command. Type 'in', 'out', or 'exit'.")


if __name__ == "__main__":
    print("Smart Parking System")
    smart_parking_system(5)
