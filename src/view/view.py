class View:

    def print_message(self, msg: str) -> str:
        return print(msg)

    def get_attribute(self):
        return input('Get word: \n')

    def print_test(self, test):
        print(test.title)
