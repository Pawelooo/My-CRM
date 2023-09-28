from src.model.generator import Generator


class Category:

    def __init__(self, name: str):
        self.id = Generator().generate_number()
        self.name = name

    def __repr__(self):
        return str({
            'name': f"{self.name}",
            'id': f"{self.id}"
        })

    def __str__(self):
        return self.name
