from src.model.generator import Generator
from src.service.tags.tag import Tag


class Question:

    def __init__(self, name: str, tag: Tag):
        self.id = Generator().generate_number()
        self.name = name
        self.number_of_fails = 0
        self.number_of_usages = 0
        self.tag = tag

    def __repr__(self):
        return {
            'name': self.name,
            'number of fails': self.number_of_fails,
            'Number of usages': self.number_of_usages,
            'Tag': self.tag,
            'id': self.id
        }
