from library import Library
from models import Book, Member

library = Library(
    book_file="Lists/Books.txt",
    member_file="Lists/Members.txt"
)


while True:

    print("\nLibrary Menu")
    print("1. List books")
    print("2. Add book")
    print("3. Add member")
    print("4. Borrow book")
    print("5. Return book")
    print("6. Exit")

    choice = input("Choose option: ")
    print("\n")

    if choice == "1":
        for book in library.books.values():
            book.display_info()

    elif choice == "2":
        book_id = input("Book ID: ")
        title = input("Title: ")
        author = input("Author: ")
        copies = int(input("Number of copies: "))

        book = Book(book_id, title, author, copies)
        library.add_book(book)

        print("Book added.")

    elif choice == "3":
        member_id = input("Member ID: ")
        name = input("Member name: ")

        member = Member(member_id, name)
        library.add_member(member)

        print("Member added.")

    elif choice == "4":
        member_id = input("Member ID: ")
        book_id = input("Book ID: ")

        result = library.borrow_book(member_id, book_id)
        print(result)

    elif choice == "5":
        member_id = input("Member ID: ")
        book_id = input("Book ID: ")

        result = library.return_book(member_id, book_id)
        print(result)

    elif choice == "6":
        break
