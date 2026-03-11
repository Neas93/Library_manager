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
            if 1 <= choice <= 11:
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

    
    elif choice == 4:
        book_id = input("Book ID to update: ")
        title = input("New title (leave blank to keep current): ")
        author = input("New author (leave blank to keep current): ")

        while True:
            try:
                copies_input = input("New number of copies (leave blank to keep current): ")

                if copies_input == "":
                    copies = None
                else:
                    copies = int(copies_input)
                break

            except ValueError:
                print("Please enter a valid number.")

        result = library.update_book(
            book_id,
            title=title if title else None,
            author=author if author else None,
            copies=copies
         )

        print(result)

    elif choice == 5:
        member_id = input("Member ID: ")
        book_id = input("Book ID: ")

        result = library.borrow_book(member_id, book_id)
        print(result)

    elif choice == 6:
        member_id = input("Member ID: ")
        book_id = input("Book ID: ")

        result = library.return_book(member_id, book_id)
        print(result)

    elif choice == 7:
        for member in library.members.values():
            member.display_info()

    elif choice == 8:
        member_id = input("Member ID: ")
        name = input("Member name: ")

        member = Member(member_id, name)
        library.add_member(member)

        print("Member added.")


    elif choice == 9:
        member_id = input("Enter the ID of the member you want to remove: ")

        result = library.remove_member(member_id)

        print(result)

    elif choice == 10:
        member_id = input("Member ID to update: ")
        name = input("New member name (leave blank to keep current): ")

        result = library.update_member(
            member_id,
            name=name if name else None
        )

        print(result)

    elif choice == 11:
        print("Bye!")
        break
