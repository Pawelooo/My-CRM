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
        obj = list(obj.values())
        return True if all([obj[i] for i in range(-1, 3)]) else False

    def update_validation(self, obj: dict[Video]):
        obj = list(obj.values())
        return True if all([obj[i] for i in range(-1, 3)]) else False

    def delete_validation(self, obj: dict[Video]):
        obj = list(obj.values())
        return True if all([obj[i] for i in range(-1, 3)]) else False


