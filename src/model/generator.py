"""
Once data with present should be found
"""
import os

from src.model.config import FILE_INDEX, FILE_ENCODING, FILE_CONFIG_LOCATION


class Generator:

    def __init__(self):
        self.root_file = os.path.dirname(os.path.abspath(__file__))
        self.dct = {}

    def generate_number(self):
        self.get_number()
        self.dct['FILE_INDEX'] = int(self.dct['FILE_INDEX'])
        self.dct['FILE_INDEX'] += 1
        self.save_number()
        return self.dct['FILE_INDEX']

    def get_number(self):
        with open(f'{self.root_file}/config.py', "r+", encoding=FILE_ENCODING) as f:
            d = f.read().rsplit('\n')[:-1]
            for i in d:
                n = i.split(" = ")
                j, t = n[0], n[1]
                self.dct[j] = t

    def save_number(self):
        with open(f'{self.root_file}/config.py', 'r+', encoding=FILE_ENCODING) as f:
            for k, v in self.dct.items():
                f.writelines(f'{k} = {v}\n')
