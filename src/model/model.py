import logging
import os
import pickle


class Model:
    def __init__(self):
        self.file_name = 'test.pkl'

    def save_to_file(self, test):
        self.check_file_is_exist()
        data_tmp = [element for element in self.get_from_file()]
        data_tmp.insert(0, test)
        with open(self.file_name, 'wb+') as handle:
            pickle.dump(data_tmp, handle)

    def get_from_file(self):
        logging.basicConfig(filename='test.pkl', level=logging.INFO)
        self.check_file_is_exist()
        with open(self.file_name, "rb+") as f:
            try:
                data = pickle.load(f, encoding='utf-8')
            except EOFError as err:
                logging.error(EOFError)
                print(err)
                data = []
        return data

    def check_file_is_exist(self):
        if self.file_name not in os.listdir():
            with open(self.file_name, 'wb+') as handle:
                pickle.dump([], handle)

def main() -> None:
    m1 = Model()
    m1.get_from_file()


if __name__ == '__main__':
    main()