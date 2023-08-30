from src.model.config import FILE_LOCATION, FILE_SUBITEM
from src.model.respository import Repository
from src.model.item import Item


class SubItemService:

    def __init__(self):
        self.repository = Repository()

    def create(self, obj: Item):
        self.repository.create(f'{FILE_LOCATION}{FILE_SUBITEM}', obj)

    def read(self, ):
        return self.repository.find_all(f'{FILE_LOCATION}{FILE_SUBITEM}')

    def update(self, obj: Item, key: str):
        self.repository.update(f'{FILE_LOCATION}{FILE_SUBITEM}', obj, key)

    def delete(self, key: str):
        self.repository.delete(f'{FILE_LOCATION}{FILE_SUBITEM}', key)

