from src.model.generator import Generator


class User:

    def __init__(self, name: str, password: str, email: str, full_name: str = None):
        self.id = Generator().generate_number()
        self.name = name
        self.password = password
        self.email = email
        self.full_name = full_name
    