from src.model.author import Author
from src.model.category import Category
from src.model.generator import Generator


class Course:

    def __init__(self, name: str, category: Category, author: Author, link: str = None, topic: str = None):
        self.id = Generator().generate_number()
        self.name = name
        self.category = category
        self.author = author
        self.link = link
        self.topic = topic
        