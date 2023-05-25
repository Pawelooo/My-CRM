from src.model.model import Model
from src.model.test import Test
from src.view.view import View


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View()

    def control(self):
        test1 = Test('Paweł', 'Rutkowski')
        test3 = Test('Python', 'Czwartek')
        test2 = Test('Zajecia', 'Nowe')
        self.model.save_to_file(test1)
        self.model.save_to_file(test2)
        self.model.save_to_file(test3)
        tests = self.model.get_from_file()
        # self.model.save_to_file()
        # self.model.get_from_file()

        for t in tests:
            self.view.print_message(t.title)
