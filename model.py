import pickle


class Model:
    def __init__(self):
        self.test = ""
        self.file_name = ''

    def set_test(self, test):
        self.test = test

    def get_test(self):
        return self.test

    def set_name_file(self, file_name):
        self.file_name = file_name

    def save_to_file(self):
        with open(self.file_name, 'wb') as handle:
            pickle.dump(self.test, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def get_from_file(self):
        with open(self.file_name, 'rb') as handle:
            return pickle.load(handle)
