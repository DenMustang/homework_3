from book import Book


class EBook(Book):
    def __init__(self, title, author, isbn, file_format):
        super().__init__(title, author, isbn)
        self.file_format = file_format

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, Format: {self.file_format}"
