from src.model.category import Category


class CategoryService:

    def __init__(self):
        self.category = None

    def create_category(self, name: str):
        self.category = Category(name)

    def read_category(self):
        return f'Name: {self.category.name}'

    def update_category(self, key: str, new_value: str):
        book = vars(self.category)
        book[key] = new_value

    def delete_category(self):
        del self.category

