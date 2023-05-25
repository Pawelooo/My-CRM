import os
import pickle

from src.model.test import Test


class Model:
    def __init__(self):
        self.file_name = 'test.txt'

    def save_to_file(self, test):
        data_tmp = []
        try:
            open(self.file_name, 'wb')
        except IOError:
            open(self.file_name, 'w+')

        else:
            data_tmp.append(test)
            data_tmp.append(self.get_from_file())
            print(data_tmp)
        with open(self.file_name, 'wb') as handle:
            pickle.dump(data_tmp, handle, protocol=pickle.HIGHEST_PROTOCOL)


    def get_from_file(self):
        with open(self.file_name, 'rb') as handle:
            try:
                return pickle.load(handle)
            except EOFError:
                pass
            return None
