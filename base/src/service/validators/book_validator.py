from base.src.model.book import Book
from base.src.model.validator import Validator


class BookValidator(Validator):

    def validate(self, obj: dict[Book], type_elm: str):
        if type_elm == 'create':
            res = self.create_validation(obj)
        if type_elm == 'update':
            res = self.update_validation(obj)
        if type_elm == 'delete':
            res = self.delete_validation(obj)
        return res

    def create_validation(self, obj: dict[Book]):
        for key, value in obj.items():
            if key in ['name', 'category', 'author', 'id']:
                if not obj[key]:
                    return False
        return True

    def update_validation(self, obj: dict[Book]):
        for key, value in obj.items():
            if key in ['name', 'category', 'author', 'id']:
                if not obj[key]:
                    return False
        return True

    def delete_validation(self, obj: dict[Book]):
        for key, value in obj.items():
            if key in ['name', 'category', 'author', 'id']:
                if not obj[key]:
                    return False
        return True


