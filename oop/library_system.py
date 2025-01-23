# library_system.py

# Base Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{__class__.__name__}: {self.title} by Author {self.author}"

# Derived Class: EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{__class__.__name__}: {self.title} by Author {self.author}, File Size: {self.file_size}KB"

# Derived Class: PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{__class__.__name__}: {self.title} by Author {self.author}, Page Count: {self.page_count}"

# Composition: Library
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only Book, EBook, or PrintBook can be added to the library.")
       
    def list_books(self):
        if not self.books:
            print("Book cannot be found.")
        for book in self.books:
            print(book)
