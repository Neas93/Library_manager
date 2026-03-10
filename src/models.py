#base_class to  avoid repition of same code
class Item_info:
    def display_info(self):
        pass
    
#class and functions for books
class Book(Item_info):
    def __init__ (self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

    def display_info(self):
        print(f"{self.book_id} | {self.title} | {self.author} | {self.copies}")


#class and functions for members
class Member(Item_info):

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def display_info(self):
        print(f"{self.member_id} | {self.name} | Borrowed: {len(self.borrowed_books)}")
        