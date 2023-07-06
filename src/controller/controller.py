from src.model.model import Model
from src.model.test import Test
from src.view.view import View


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View()

    def control(self):
        pass