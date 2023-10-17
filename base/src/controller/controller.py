import logging

from base.src.model.model import Model
<<<<<<< HEAD
<<<<<<< HEAD
=======
from base.src.model.test import Test
>>>>>>> dd4209d (#96 module 1 basic crud rest api)
=======
from base.src.model.test import Test
>>>>>>> dd4209d12a5419d449005abe09a2927b86221da9
from base.src.view.view import View


class Controller:

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.model = Model()
        self.view = View()

    def control(self):
        pass
