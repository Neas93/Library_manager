from library import Library
from models import Book, Member
from utils import menu

library = Library(
    book_file="Lists/Books.txt",
    member_file="Lists/Members.txt"
)

while True:

    menu()
    while True:
        try:
            choice = int(input("Choose option: "))
            if 1 <= choice <= 9:
                break
            else:
                print("Please enter a number from the menu")
        except ValueError:
            print("Please only use numbers to choose")

    
    print("=" * 40 + "\n")

    if choice == 1:
        for book in library.books.values():
            book.display_info()

    elif choice == 2:
        book_id = input("Book ID: ")
        title = input("Title: ")
        author = input("Author: ")
        while True:
            try:
                copies = int(input("Number of copies: "))
                break
            except ValueError as e:
                print("Please enter a valid number")

        book = Book(book_id, title, author, copies)
        library.add_book(book)

        print("Book added.")

    elif choice == 3:
        book_id = input("Enter ID of the book you want to remove: ")

        result = library.remove_book(book_id)

        print(result)

    elif choice == "4":
        member_id = input("Member ID: ")
        book_id = input("Book ID: ")

        result = library.borrow_book(member_id, book_id)
        print(result)

    elif choice == 5:
        member_id = input("Member ID: ")
        book_id = input("Book ID: ")

        result = library.return_book(member_id, book_id)
        print(result)

    elif choice == 6:
        member_id = input("Member ID: ")
        name = input("Member name: ")

        member = Member(member_id, name)
        library.add_member(member)

        print("Member added.")

    elif choice == 7:
        for member in library.members.values():
            member.display_info()

    elif choice == 8:
        member_id = input("Enter the ID of the member you want to remove: ")

        result = library.remove_member(member_id)

        print(result)

    elif choice == 9:
        print("Bye!")
        break
