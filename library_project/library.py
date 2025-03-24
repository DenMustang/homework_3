class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def lend_book(self, book, member):
        if book.available:
            book.mark_unavailable()
            member.borrow_book(book)
        else:
            print(f"Book '{book.title}' is not available.")

    def receive_book(self, book, member):
        book.mark_available()
        member.return_book(book)
