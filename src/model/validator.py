from abc import ABC, abstractmethod


class Validator(ABC):

    @abstractmethod
    def validate(self, obj, type_elm):
        pass



