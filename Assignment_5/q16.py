"""
Q16. Library Management System
Store books using a dictionary, issue and return books, and use functions for modular design.
"""

books = {
    "Python Basics": {"copies": 3},
    "Data Structures": {"copies": 2},
    "Algorithms": {"copies": 1},
}


def display_books():
    print("Available books:")
    for title, info in books.items():
        print(f"- {title}: {info['copies']} copies")


def issue_book(title):
    if title not in books:
        print("Book not found.")
        return False
    if books[title]["copies"] <= 0:
        print("Book is currently unavailable.")
        return False
    books[title]["copies"] -= 1
    print(f"Issued: {title}")
    return True


def return_book(title):
    if title not in books:
        books[title] = {"copies": 0}
    books[title]["copies"] += 1
    print(f"Returned: {title}")


if __name__ == "__main__":
    display_books()
    issue_book("Python Basics")
    issue_book("Algorithms")
    return_book("Algorithms")
    print()
    display_books()
