class Item_info:
    def display_info(self):
        pass

class Book(Item_info):
    def __init__ (self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

    def display_info(self):
        print(f"{self.book_id} | {self.title} | {self.author} | {self.copies}")
