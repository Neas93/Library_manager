import unittest
from src.library import Library
from src.models import Book, Member

class TestLibraryClass(unittest.TestCase):

    def test_search_book_by_id(self):
        library = Library()
        library.books["B001"] = Book("B001", "1984", "George Orwell", 10)

        book = library.search_book_by_id("B001")

        self.assertIsNotNone(book)
        self.assertEqual(book.title, "1984")

    def test_borrow_book(self):
        library = Library()
        library.books["B001"] = Book("B001", "1984", "George Orwell", 2)

        member = Member("M001", "Nicklas")
        library.members["M001"] = member

        result = library.borrow_book("M001", "B001")

        self.assertEqual(result, "Book borrowed successfully")
        self.assertEqual(library.books["B001"].copies, 1)
        self.assertIn("B001", member.borrowed_books)

if __name__ == "__main__":
    unittest.main()

    