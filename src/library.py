from models import Book, Member

class Library:
    def __init__(self, filepath=None):
        self.books = {}
        self.members = {}

        if filepath:
            self.load_books_from_file(filepath)

    def load_books_from_file(self,filepath):
        with open(filepath, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                book_id, title, author, copies = line.split(";")
                book = Book(book_id, title, author, int(copies))
                self.books[book_id] = book


    def search_book_by_id(self, book_id):
        return self.books.get(book_id)
    
    
    def search_book_by_title(self, title):
        for book in self.books.values():
            if book.title.lower() == title.lower():
                return book
        return None
    
    
    def borrow_book(self, member_id, book_id):
        member = self.members.get(member_id)
        book = self.books.get(book_id)

        if member is None:
            return "Member not found"

        if book is None:
            return "Book not found"

        if book.copies <= 0:
            return "No copies available"

        member.borrowed_books.append(book_id)
        book.copies -= 1
        return "Book borrowed successfully"