import os
import pickle

from src.model.test import Test


class Model:
    def __init__(self):
        self.file_name = 'test.pkl'

    def save_to_file(self, test):
        data_tmp = [element for element in self.get_from_file()]
        data_tmp.insert(0, test)
        with open(self.file_name, 'wb+') as handle:
            pickle.dump(data_tmp, handle)

    def get_from_file(self):
        with open(self.file_name, "rb+") as f:
            try:
                data = pickle.load(f, encoding='utf-8')
            except EOFError:
                data = []
        return data

