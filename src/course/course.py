from src.author.author import Author
from src.category.category import Category


class Course:

    def __init__(self, name: str, category: Category, author: Author, link: str = None, topic: str = None):
        self.name = name
        self.category = category
        self.author = author
        self.link = link
        self.topic = topic
        
