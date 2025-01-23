class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
    
    # def __del__(self):
    #     print(f"Deleting {self.title}")
    
    # def __str__(self):
    #     return f"{self.title} by {self.author}, published in {self.year}"
    
    # def __repr__(self):
    #     return f"Book('{self.title}', '{self.author}', {self.year})"

class EBook(Book):
    def __init__(self, title, author, file_size):
       super().__init__(title, author)
       self.file_size = file_size

        
class PrintBook(Book):
    def __ini__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            
    def list_books(self):
        for book in self.books:
            print(book)