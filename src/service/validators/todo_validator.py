from src.model.item import ToDo
from src.model.validator import Validator


class ToDoValidator(Validator):

    def validate(self, obj: dict[ToDo], type_elm: str):
        if type_elm == 'create':
            self.create_validation(obj)
        if type_elm == 'update':
            self.update_validation(obj)
        if type_elm == 'delete':
            self.delete_validation(obj)

    def create_validation(self, obj: dict[ToDo]):
        obj = list(obj.values())
        return True if all([obj[i] for i in range(-1, 1)]) else False

    def update_validation(self, obj: dict[ToDo]):
        obj = list(obj.values())
        return True if all([obj[i] for i in range(-1, 1)]) else False

    def delete_validation(self, obj: dict[ToDo]):
        obj = list(obj.values())
        return True if all([obj[i] for i in range(-1, 1)]) else False


