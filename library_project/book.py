class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def mark_unavailable(self):
        self.available = False

    def mark_available(self):
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Unavailable"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {status}"
