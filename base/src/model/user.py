from base.src.model.generator import Generator


class User:

    def __init__(self, name: str, password: str, email: str, full_name: str = None):
        self.id = Generator().generate_number()
        self.name = name
        self.password = password
        self.email = email
        self.full_name = full_name

    def __repr__(self):
        return {
            "name": f"{self.name}",
            "password": f"{self.password}",
            "email": f"{self.email}",
            "full_name": f"{self.full_name}" if self.full_name else "",
            "id": f"{self.id}"
        }
    
