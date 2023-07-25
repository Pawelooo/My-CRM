from src.model.book import Book
from src.model.validator import Validator


class BookValidator(Validator):

    def validate(self, obj: dict[Book], type_elm: str):
        if type_elm == 'create':
            self.create_validation(obj)
        if type_elm == 'update':
            self.update_validation(obj)
        if type_elm == 'delete':
            self.delete_validation(obj)

    def create_validation(self, obj: dict[Book]):
        obj = list(obj.values())
        return True if all([obj[i] for i in range(-1, 3)]) else False

    def update_validation(self, obj: dict[Book]):
        obj = list(obj.values())
        return True if all([obj[i] for i in range(-1, 3)]) else False

    def delete_validation(self, obj: dict[Book]):
        obj = list(obj.values())
        return True if all([obj[i] for i in range(-1, 3)]) else False


