import logging
import os
import pickle

from base.src.model.config import FILE_ENCODING, FILE_MODEL


class Model:

    def save_to_file(self, test):
        self.check_file_is_exist()
        data_tmp = [element for element in self.get_from_file()]
        data_tmp.insert(0, test)
        with open(FILE_MODEL, 'wb+') as handle:
            pickle.dump(data_tmp, handle)

    def get_from_file(self, ):
        self.check_file_is_exist()
        data = []
        try:
            with open(FILE_MODEL, "rb+") as f:
                data = pickle.load(f, encoding=FILE_ENCODING)
        except EOFError and FileNotFoundError as err:
            logging.error(err)
            return data
        else:
            return data

    def check_file_is_exist(self):
        if FILE_MODEL not in os.listdir():
            with open(FILE_MODEL, 'wb+') as handle:
                pickle.dump([], handle)
