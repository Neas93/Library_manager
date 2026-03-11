import unittest
from src.library import Library
from src.models import Book, Member

class TestLibraryClass(unittest.TestCase):


    def test_borrow_book(self):
        library = Library()
        library.books["B001"] = Book("B001", "1984", "George Orwell", 2)

        member = Member("M001", "Nicklas")
        library.members["M001"] = member

        result = library.borrow_book("M001", "B001")

        self.assertEqual(result, "Book borrowed successfully")
        self.assertEqual(library.books["B001"].copies, 1)
        self.assertIn("B001", member.borrowed_books)

    def test_return_book(self):

        library = Library()

        library.books["B001"] = Book("B001", "1984", "George Orwell", 1)

        member = Member("M001", "Nicklas")
        library.members["M001"] = member

        member.borrowed_books.append("B001")

        result = library.return_book("M001", "B001")

        self.assertEqual(result, "Book returned successfully")
        self.assertEqual(library.books["B001"].copies, 2)
        self.assertNotIn("B001", member.borrowed_books)

    def test_rmv_book(self):
        library = Library()
        library.books["B001"] = Book("B001", "1984", "George Orwell", 10)

        result = library.remove_book("B001")
        self.assertEqual(result, "Book removed succesfully")
        self.assertNotIn("B001", library.books)

    def test_rmv_book_not_found(self):
        library = Library()

        result = library.remove_book("B999")

        self.assertEqual(result, "Book not found")


    def test_rmv_member(self):
        library = Library()
        library.members["M001"] = Member("M001", "Nicklas")

        result = library.remove_member("M001")

        self.assertEqual(result, "Member removed successfully")
        self.assertNotIn("M001", library.members)


    def test_rmv_member_not_found(self):
        library = Library()

        result = library.remove_member("M999")

        self.assertEqual(result, "Member not found")

if __name__ == "__main__":
    unittest.main()

    