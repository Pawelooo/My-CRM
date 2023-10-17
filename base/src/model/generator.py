"""
Once data with present should be found
"""
import os

from base.src.model.config import FILE_INDEX, FILE_ENCODING, FILE_CONFIG_LOCATION, \
    FILE_INDEX_STR, READ_PLUS, FILE_CONFIG


class Generator:

    def __init__(self):
        self.root_file = os.path.dirname(os.path.abspath(__file__))
        self.dct = {}

    def generate_number(self):
        self.get_number()
        self.dct[FILE_INDEX_STR] = int(self.dct[FILE_INDEX_STR])
        self.dct[FILE_INDEX_STR] += 1
        self.save_number()
        return self.dct[FILE_INDEX_STR]

    def get_number(self):
        with open(f'{self.root_file}/{FILE_CONFIG}', READ_PLUS, encoding=FILE_ENCODING) as f:
            d = f.read().rsplit('\n')[:-1]
            for i in d:
                n = i.split(" = ")
                j, t = n[0], n[1]
                self.dct[j] = t

    def save_number(self):
        with open(f'{self.root_file}/{FILE_CONFIG}', READ_PLUS, encoding=FILE_ENCODING) as f:
            for k, v in self.dct.items():
                f.writelines(f'{k} = {v}\n')
