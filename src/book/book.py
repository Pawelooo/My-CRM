from src.author.author import Author
from src.category.category import Category


class Book:

    def __init__(self, name: str, category: Category, author: Author,
                 link: str = None, topic: str = None, version: str = None,
                 page_count: str = None, date_publish: str = None):
        self.name = name
        self.category = category
        self.author = author
        self.link = link
        self.topic = topic
        self.version = version
        self.page_count = page_count
        self.date_publish = date_publish
        