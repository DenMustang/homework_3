Exercise 1: Creating the Book Class (book.py) 📌 Objective: Create a class Book to represent a book in the library.

Tasks:

Define a Book class with the following attributes: title (str) author (str) isbn (str) available (bool, default: True) Add a method mark_unavailable() to set available to False. Add a method mark_available() to set available to True. Implement the str method to print book details.

📂 File Structure:

library_project/

── book.py

Type Markdown and LaTeX: 𝛼2

from book import Book​book1 = Book("1984", "George Orwell", "1234567890") print(book1) # Should display book details​book1.mark_unavailable() print(book1.available) # Should print False​Exercise 2: Creating the Member Class (member.py) 📌 Objective: Define a Member class representing library members.

Tasks:

Attributes: name (str) member_id (str) borrowed_books (list, default: empty list) Method borrow_book(book) to add a book to borrowed_books. Method return_book(book) to remove a book from borrowed_books. Implement str to display member details. 📂 File Structure:

library_project/

── book.py

── member.py

from member import Member from book import Book

member1 = Member("Alice", "M001") book1 = Book("The Catcher in the Rye", "J.D. Salinger", "9876543210")

member1.borrow_book(book1) print(member1) # Should display borrowed books

Exercise 3: Creating the Library Class (library.py) 📌 Objective: Define a Library class to manage books and members.

Tasks:

Attributes: books (list of Book objects) members (list of Member objects) Method add_book(book) to add a book to the library. Method add_member(member) to register a member. Method lend_book(book, member) to allow borrowing if available. Method receive_book(book, member) to return a borrowed book. 📂 File Structure:

library_project/

── book.py

── member.py

── library.py

from library import Library from book import Book from member import Member

lib = Library() book1 = Book("Moby Dick", "Herman Melville", "1122334455") member1 = Member("Bob", "M002")

lib.add_book(book1) lib.add_member(member1) lib.lend_book(book1, member1) print(book1.available) # Should be False

Exercise 4: Creating a main.py File to Use the Library System 📌 Objective: Write a script (main.py) to interact with the library system.

Tasks:

Create books and members. Register them in the library. Borrow and return books. Print book and member details. 📂 File Structure:

library_project/

── book.py

── member.py

── library.py

── main.py

from book import Book from member import Member from library import Library

Create a Library lib = Library()

Add Books book1 = Book("To Kill a Mockingbird", "Harper Lee", "5544332211") book2 = Book("Pride and Prejudice", "Jane Austen", "9988776655")

lib.add_book(book1) lib.add_book(book2)

Add Members member1 = Member("Charlie", "M003") lib.add_member(member1)

Borrow and Return Books lib.lend_book(book1, member1) print(member1) # Should show borrowed books

lib.receive_book(book1, member1) print(book1.available) # Should be True

Exercise 5: Enhancing the Library System with Inheritance (ebook.py) 📌 Objective: Extend the Book class to create an EBook class.

Tasks:

EBook should inherit from Book. Add an extra attribute file_format (e.g., "PDF"). Override str to include file format. 📂 File Structure:

library_project/

── book.py

── member.py

── library.py

── ebook.py

── main.py
