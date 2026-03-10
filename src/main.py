from library import Library

library = Library(
    book_file="Lists/Books.txt",
    member_file="Lists/Members.txt"
)

print("Books:")
for book in library.books.values():
    book.display_info()

print("\nMembers:")
for member in library.members.values():
    member.display_info()