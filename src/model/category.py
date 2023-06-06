from src.model.generator import Generator


class Category:

    def __init__(self, name: str):
        self.id = Generator().generate_number()
        self.name = name