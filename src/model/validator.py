from abc import ABC, abstractmethod

from src.model.author import Author


class Validator(ABC):

    @abstractmethod
    def validate(self, obj, type_elm):
        pass



