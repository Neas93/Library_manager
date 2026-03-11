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

if __name__ == "__main__":
    unittest.main()

    