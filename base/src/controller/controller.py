import logging

from base.src.model.model import Model
from base.src.model.test import Test
from base.src.view.view import View


class Controller:

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.model = Model()
        self.view = View()

    def control(self):
        pass
