from src.model.generator import Generator


class Status:

    def __init__(self, name: str):
        self.id = Generator().generate_number()
        self.name = name

    def __repr__(self):
        return {
            'name': self.name,
            'id': self.id
        }
