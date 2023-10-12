from src.model.validator import Validator
from validator_collection import validators

class Validations:

    def __init__(self):
        self._validator = None

    @property
    def validator(self) -> Validator:
        return self._validator

    @validator.setter
    def validator(self, validator: Validator):
        self._validator = validator

    def validate(self, obj, type_elm):
        self.validator.validate(obj, type_elm)
