"""
Q3. Event Registration System
Store participants using a set, ensure no duplicates, and convert final data into tuple format.
"""

participants = set()


def register_participant(name):
    normalized = name.strip().title()
    if normalized in participants:
        print(f"Participant '{normalized}' is already registered.")
        return False
    participants.add(normalized)
    print(f"Registered: {normalized}")
    return True


def finalize_registration():
    return tuple(sorted(participants))


if __name__ == "__main__":
    print("Event Registration System")
    register_participant("Aarav")
    register_participant("Meera")
    register_participant("aarav")
    register_participant("Nisha")
    participant_list = finalize_registration()
    print("Final participant list (tuple):", participant_list)
