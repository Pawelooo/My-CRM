from base.src.model.video import Video
from base.src.model.validator import Validator


class VideoValidator(Validator):

    def validate(self, obj: dict[Video], type_elm: str):
        if type_elm == 'create':
            self.create_validation(obj)
        if type_elm == 'update':
            self.update_validation(obj)
        if type_elm == 'delete':
            self.delete_validation(obj)

    def create_validation(self, obj: dict[Video]):
        for key, value in obj.items():
            if key in ['name', 'category', 'author', 'id']:
                if not obj[key]:
                    return False
        return True

    def update_validation(self, obj: dict[Video]):
        for key, value in obj.items():
            if key in ['name', 'category', 'author', 'id']:
                if not obj[key]:
                    return False
        return True

    def delete_validation(self, obj: dict[Video]):
        for key, value in obj.items():
            if key in ['name', 'category', 'author', 'id']:
                if not obj[key]:
                    return False
        return True


