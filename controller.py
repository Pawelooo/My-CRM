from model import Model
from view import View


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View()

    def control(self):
        self.model.set_test(self.view.get_attribute())
        self.view.print_message(self.model.get_test())
