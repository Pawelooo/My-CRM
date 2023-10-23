from base.src.model.user import User
from base.src.model.validator import Validator


class UserValidator(Validator):

    def validate(self, obj: dict[User], type_elm: str):
        if type_elm == 'create':
            self.create_validation(obj)
        if type_elm == 'update':
            self.update_validation(obj)
        if type_elm == 'delete':
            self.delete_validation(obj)

    def create_validation(self, obj: dict[User]):
        for key, value in obj.items():
            if key in ['name', 'password', 'email', 'id']:
                if not obj[key]:
                    return False
        return True

    def update_validation(self, obj: dict[User]):
        for key, value in obj.items():
            if key in ['name', 'password', 'email', 'id']:
                if not obj[key]:
                    return False
        return True

    def delete_validation(self, obj: dict[User]):
        for key, value in obj.items():
            if key in ['name', 'password', 'email', 'id']:
                if not obj[key]:
                    return False
        return True


