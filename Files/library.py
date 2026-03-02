from models import Book

class Library:
    def __init__(self):
        self.books = {}
        self.load_books_from_file("Lists/Books.txt")

    def load_books_from_file(self,filepath):
        with open(filepath, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                book_id, title, author, copies = line.split(";")
                book = Book(book_id, title, author, int(copies))
                self.books[book_id] = book