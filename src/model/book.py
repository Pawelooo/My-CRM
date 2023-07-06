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

    def __repr__(self):
        return {
            'name': self.name if self.name is not None else '',
            'category': self.category if self.category is not None else '',
            'author': self.author if self.author is not None else '',
            'link': self.link if self.link is not None else '',
            'topic': self.topic if self.topic is not None else '',
            'version': self.version if self.version is not None else '',
            'page_count': self.page_count if self.page_count is not None else '',
            'date_publish': self.date_publish if self.date_publish is not None else '',
            'id': str(self.id)
        }