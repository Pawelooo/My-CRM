<<<<<<< HEAD
=======
import json

>>>>>>> dd4209d12a5419d449005abe09a2927b86221da9
from base.src.model.generator import Generator


class Author:

    def __init__(self, name: str, surname: str, website: str = None, country: str = None, topic: str = None):
        self.id = Generator().generate_number()
        self.name = name
        self.surname = surname
        self.website = website
        self.country = country
        self.topic = topic
