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
            "name": f"{self.name}",
            "number_of_fails": f"{self.number_of_fails}",
            "Number_of_usages": f"{self.number_of_usages}",
            "Tag": f"{self.tag}",
            "id": f"{self.id}"
        }
