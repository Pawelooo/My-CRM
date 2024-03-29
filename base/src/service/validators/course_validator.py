from base.src.model.course import Course
from base.src.model.validator import Validator


class CourseValidator(Validator):

    def validate(self, obj: dict[Course], type_elm: str):
        res = None
        if type_elm == 'create':
            res = self.create_validation(obj)
        if type_elm == 'update':
            res = self.update_validation(obj)
        if type_elm == 'delete':
            res = self.delete_validation(obj)
        return res

    def create_validation(self, obj: dict[Course]):
        for key, value in obj.items():
            if key in ['name', 'category', 'author', 'id']:
                if not obj[key]:
                    return False
        return True

    def update_validation(self, obj: dict[Course]):
        for key, value in obj.items():
            if key in ['name', 'category', 'author', 'id']:
                if not obj[key]:
                    return False
        return True

    def delete_validation(self, obj: dict[Course]):
        for key, value in obj.items():
            if key in ['name', 'category', 'author', 'id']:
                if not obj[key]:
                    return False
        return True


