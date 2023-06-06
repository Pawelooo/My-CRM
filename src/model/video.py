from datetime import datetime

from src.model.author import Author
from src.category.category import Category


class Video:

    def __init__(self, name: str, category: Category, author: Author, link: str = None,
                 topic: str = None, version: str = None, date_publication: datetime = None):
        self.name = name
        self.category = category
        self.author = author
        self.link = link
        self.topic = topic
        self.version = version
        self.date_publication = date_publication
        