from library import Library

lib = Library()

print("ID | Title | Title | Author | Copies\n")
print ("-" * 50)
for book in lib.books.values():
    book.display_info()