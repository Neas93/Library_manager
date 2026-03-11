from models import Book, Member

class Library:
    def __init__(self, book_file=None, member_file=None):
        self.books = {}
        self.members = {}
        self.book_file = book_file
        self.member_file = member_file

        if book_file:
            self.load_books_from_file(book_file)

        if member_file:
            self.load_members_from_file(member_file)

#filebased functions

    def load_books_from_file(self,filepath):
        with open(filepath, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                book_id, title, author, copies = line.split(";")
                book = Book(book_id, title, author, int(copies))
                self.books[book_id] = book

    def load_members_from_file(self, filepath):
        with open(filepath, "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split(";")

                member_id = parts[0]
                name = parts[1]

                borrowed_books = []
                if len(parts) > 2 and parts[2]:
                    borrowed_books = parts[2].split(",")

                member = Member(member_id, name, borrowed_books)
                self.members[member_id] = member

    def save_books_to_file(self):
        if not self.book_file:
            return

        with open(self.book_file, "w") as file:
            for book in self.books.values():
                file.write(f"{book.book_id};{book.title};{book.author};{book.copies}\n")
    
    def save_members_to_file(self):
        if not self.member_file:
            return

        with open(self.member_file, "w") as file:
            for member in self.members.values():
                borrowed = ",".join(member.borrowed_books)
                file.write(f"{member.member_id};{member.name};{borrowed}\n")
    
#Book & Member related functions
   
    def add_book(self, book):
        self.books[book.book_id] = book
        self.save_books_to_file()
      
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

        self.save_books_to_file()
        self.save_members_to_file()

        return "Book borrowed successfully"

    def return_book(self, member_id, book_id):

        member = self.members.get(member_id)
        book = self.books.get(book_id)

        if member is None:
            return "Member not found"

        if book is None:
            return "Book not found"

        if book_id not in member.borrowed_books:
            return "Book not borrowed by this member"

        member.borrowed_books.remove(book_id)
        book.copies += 1

        self.save_books_to_file()
        self.save_members_to_file()

        return "Book returned successfully"
    
    def update_book(self, book_id, title=None, author=None, copies=None):
        book = self.books.get(book_id)

        if book is None:
            return "Book not found"
        
        if title:
            book.title = title

        if author:
            book.author = author

        if copies is not None:
            book.copies = copies

        self.save_books_to_file()
        return "Book updated"

    def add_member(self, member):
        self.members[member.member_id] = member
        self.save_members_to_file()

    def update_member(self, member_id, name=None):
        member = self.members.get(member_id)

        if member is None:
            return "Member not found"
        
        if name:
            member.name = name

        self.save_members_to_file()
        return "Member updated"

#Functions to remove books/members

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            self.save_books_to_file()
            return "Book removed succesfully"
        return "Book not found"
    
    def remove_member(self, member_id):
        if member_id in self.members:
            del self.members[member_id]
            self.save_members_to_file()
            return "Member removed successfully"
        return "Member not found"
