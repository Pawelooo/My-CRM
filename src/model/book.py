from src.model.author import Author
from src.model.category import Category
from src.model.generator import Generator


class Book:

    def __init__(self, name: str, category: Category, author: Author,
                 link: str = None, topic: str = None, version: str = None,
                 page_count: str = None, date_publish: str = None):
        self.id = Generator().generate_number()
        self.name = name
        self.category = category
        self.author = author
        self.link = link
        self.topic = topic
        self.version = version
        self.page_count = page_count
        self.date_publish = date_publish
        