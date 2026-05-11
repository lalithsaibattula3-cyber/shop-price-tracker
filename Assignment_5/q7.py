"""
Q7. File Backup Simulation (Recursion)
Represent folders using nested dictionaries and print all file paths recursively.
"""

backup_structure = {
    "Documents": {
        "resume.pdf": None,
        "projects": {
            "proposal.docx": None,
            "code": {
                "app.py": None,
                "utils.py": None,
            },
        },
    },
    "Photos": {
        "vacation": {
            "beach.png": None,
            "mountain.jpg": None,
        },
    },
}


def print_file_paths(folder, parent_path=""):
    for name, node in folder.items():
        path = parent_path + "/" + name if parent_path else name
        if isinstance(node, dict):
            print_file_paths(node, path)
        else:
            print(path)


if __name__ == "__main__":
    print("File Backup Paths")
    print_file_paths(backup_structure)
