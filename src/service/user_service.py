from src.model.user import User


class UserService:

    def __init__(self):
        self.user = None

    def create_user(self, name: str, password: str, email: str, full_name: str = None):
        self.user = User(name, password, email, full_name)

    def read_user(self):
        return f'Name: {self.user.name}, Password: {self.user.password}, E-mail: {self.user.email}, ' \
               f'Full name: {self.user.full_name}'

    def update_user(self, key: str, new_value: str):
        user = vars(self.user)
        user[key] = new_value

    def delete_user(self):
        del self.user


