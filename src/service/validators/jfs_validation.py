from typing import List

from src.model.status import Status
from src.model.validator import Validator


class JfsValidator(Validator):

    def validate(self, attributes: List[str], type_elm: str):
        if type_elm == 'create':
            self.create_validation(attributes)
        if type_elm == 'update':
            self.update_validation(attributes)

    def create_validation(self, attributes: List[str]):
        return True if all([True if isinstance(obj, str) else False for obj in attributes]) else False

    def update_validation(self, attributes: List[str]):
        return True if all([True if isinstance(obj, str) else False for obj in attributes]) else False

    def read_validation(self, attributes: List[str]):
        return True if all([True if isinstance(obj, str) else False for obj in attributes]) else False





