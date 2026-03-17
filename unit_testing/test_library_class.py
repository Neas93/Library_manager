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

    def test_search_books_found(self):
        library = Library()

        book = Book("B001", "Harry Potter", "J.K. Rowling", 3)
        library.books["B001"] = book

        results = library.search_book("harry")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Harry Potter")

    def test_search_books_not_found(self):
        library = Library()

        book = Book("B001", "Harry Potter", "J.K. Rowling", 3)
        library.books["B001"] = book

        results = library.search_book("dune")

        self.assertEqual(results, [])
    

    def test_rmv_book(self):
        library = Library()
        library.books["B001"] = Book("B001", "1984", "George Orwell", 10)

        result = library.remove_book("B001")
        self.assertEqual(result, "Book removed succesfully")
        self.assertNotIn("B001", library.books)

    def test_update_book(self):

        library = Library()

        book = Book("B001", "Old Title", "Author", 3)
        library.books["B001"] = book

        result = library.update_book("B001", title="New Title")

        self.assertEqual(result, "Book updated")
        self.assertEqual(library.books["B001"].title, "New Title")

    def test_rmv_book_not_found(self):
        library = Library()

        result = library.remove_book("B999")

        self.assertEqual(result, "Book not found")

    def test_update_member(self):

        library = Library()

        member = Member("M001", "Old Name")
        library.members["M001"] = member

        result = library.update_member("M001", name="New Name")

        self.assertEqual(result, "Member updated")
        self.assertEqual(library.members["M001"].name, "New Name")

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

    