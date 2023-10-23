from back.resume.models import Item
from base.src.model.course import Course
from base.src.model.validator import Validator


class ItemValidator(Validator):

    def validate(self, obj: dict[Item], type_elm: str):
        if type_elm == 'create':
            res = self.create_validation(obj)
        if type_elm == 'update':
            res = self.update_validation(obj)
        if type_elm == 'delete':
            res = self.delete_validation(obj)
        return res

    def create_validation(self, obj: dict[Item]):
        for key, value in obj.items():
            if key in ['name', "title", "description", 'category', "name_file",
                       'deadline', 'assignee', 'id']:
                if not obj[key]:
                    return False
        return True

    def update_validation(self, obj: dict[Item]):
        for key, value in obj.items():
            if key in ['name', "title", "description", 'category', "name_file",
                       'deadline', 'assignee', 'id']:
                if not obj[key]:
                    return False
        return True

    def delete_validation(self, obj: dict[Item]):
        for key, value in obj.items():
            if key in ['name', "title", "description", 'category', "name_file",
                       'deadline', 'assignee', 'id']:
                if not obj[key]:
                    return False
        return True


