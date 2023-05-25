import unittest

from model import Model


class File(unittest.TestCase):

    def test_file_value(self):
        self.model = Model()
        self.model.test = "Nowe"
        self.model.file_name = 'test.txt'
        self.model.save_to_file()
        self.assertEquals(self.model.get_from_file(), self.model.test)


if __name__ == '__main__':
    unittest.main()
