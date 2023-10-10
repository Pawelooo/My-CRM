from datetime import datetime

from base.src.model.author import Author
from base.src.model.category import Category
from base.src.model.generator import Generator


class Video:

    def __init__(self, name: str, category: Category, author: Author, link: str = None,
                 topic: str = None, version: str = None, date_publication: datetime = None):
        self.id = Generator().generate_number()
        self.name = name
        self.category = category
        self.author = author
        self.link = link
        self.topic = topic
        self.version = version
        self.date_publication = date_publication

    def __repr__(self):
        return str({
            "name": f"{self.name}",
            "category": f"{self.category}",
            "author": f"{self.author}",
            "link": f"{self.link}" if self.link else "",
            "topic": f"{self.topic}" if self.topic else "",
            "version": f"{self.version}" if self.version else "",
            "date publication": f"{self.date_publication}" if self.date_publication else "",
            "id": f"{self.id}"
        })
        