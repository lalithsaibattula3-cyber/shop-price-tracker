"""
Q14. Smart Traffic System
Simulate traffic lights using loops, conditions, and break.
"""

LIGHT_SEQUENCE = ["Green", "Yellow", "Red"]
DURATIONS = {"Green": 5, "Yellow": 2, "Red": 4}


def run_traffic_simulation(cycles=3):
    for cycle in range(1, cycles + 1):
        print(f"Cycle {cycle}")
        for light in LIGHT_SEQUENCE:
            print(f"Light: {light} ({DURATIONS[light]} seconds)")
            if light == "Red" and cycle == cycles:
                print("Simulation complete: stopping at red light.")
                break
        print("---")


if __name__ == "__main__":
    run_traffic_simulation()
