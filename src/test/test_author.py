import unittest

from src.model.author import Author


class TestAuthor(unittest.TestCase):

    def test_create(self):
        self.assertFalse(Author('pawel', 'r'))

    def test_new(self):
        a = 1
        b = 2
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
