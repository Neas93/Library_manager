import unittest
from src.models import Member, Book


class TestBookClass(unittest.TestCase):

    def test_book_creation(self):
        book = Book("B001", "1984", "George Orwell", 10)

        self.assertEqual(book.book_id, "B001")
        self.assertEqual(book.title, "1984")
        self.assertEqual(book.author, "George Orwell")
        self.assertEqual(book.copies, 10)



class TestMemberClass(unittest.TestCase):

    def test_member_creation(self):
        member = Member("M001", "Nicklas")

        self.assertEqual(member.member_id, "M001")
        self.assertEqual(member.name, "Nicklas")
        self.assertEqual(member.borrowed_books, [])

if __name__ == "__main__":
    unittest.main()