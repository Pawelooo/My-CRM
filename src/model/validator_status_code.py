from abc import ABC, abstractmethod


class ValidatorStatus(ABC):

    @abstractmethod
    def validate(self, obj):
        pass