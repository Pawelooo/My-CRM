from back.resume.models import SubItem
from base.src.model.course import Course
from base.src.model.validator import Validator


class SubItemValidator(Validator):

    def validate(self, obj: dict[SubItem], type_elm: str):
        res = None
        if type_elm == 'create':
            res = self.create_validation(obj)
        if type_elm == 'update':
            res = self.update_validation(obj)
        if type_elm == 'delete':
            res = self.delete_validation(obj)
        return res

    def create_validation(self, obj: dict[SubItem]):
        for key, value in obj.items():
            if key in ['name', 'title', 'title', 'id_item', 'name_file', 'id']:
                if not obj[key]:
                    return False
        return True

    def update_validation(self, obj: dict[SubItem]):
        for key, value in obj.items():
            if key in ['name', 'title', 'title', 'id_item', 'name_file', 'id']:
                if not obj[key]:
                    return False
        return True

    def delete_validation(self, obj: dict[SubItem]):
        for key, value in obj.items():
            if key in ['name', 'title', 'title', 'id_item', 'name_file', 'id']:
                if not obj[key]:
                    return False
        return True


