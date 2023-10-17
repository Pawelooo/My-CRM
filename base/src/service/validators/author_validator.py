<<<<<<< HEAD
=======
from abc import ABC

<<<<<<< HEAD
>>>>>>> dd4209d (#96 module 1 basic crud rest api)
=======
>>>>>>> dd4209d12a5419d449005abe09a2927b86221da9
from base.src.model.author import Author
from base.src.model.validator import Validator


class AuthorValidator(Validator):

    def validate(self, obj: dict[Author], type_elm: str):
        if type_elm == 'create':
            self.create_validation(obj)
        if type_elm == 'update':
            self.update_validation(obj)
        if type_elm == 'delete':
            self.delete_validation(obj)

    def create_validation(self, obj: dict[Author]):
        obj = list(obj.values())
        return True if all([obj[i] for i in range(-1, 2)]) else False

    def update_validation(self, obj: dict[Author]):
        obj = list(obj.values())
        return True if all([obj[i] for i in range(-1, 2)]) else False

    def delete_validation(self, obj: dict[Author]):
        obj = list(obj.values())
        return True if all([obj[i] for i in range(-1, 2)]) else False


