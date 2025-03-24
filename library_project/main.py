from book import Book
from ebook import EBook
from library import Library
from member import Member

lib = Library()

book1 = Book("To Kill a Mockingbird", "Harper Lee", "5544332211")
book2 = Book("Pride and Prejudice", "Jane Austen", "9988776655")
lib.add_book(book1)
lib.add_book(book2)

member1 = Member("Charlie", "M003")
lib.add_member(member1)

lib.lend_book(book1, member1)
print(member1)

lib.receive_book(book1, member1)
print(book1.available)

ebook1 = EBook("Python 101", "John Doe", "4455667788", "PDF")
print(ebook1)
