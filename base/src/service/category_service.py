from base.src.model.category import Category
from base.src.model.config import FILE_LOCATION, FILE_CATEGORY_NAME, FILE_AUTHOR_NAME
from base.src.model.respository import Repository


class CategoryService:

    def __init__(self):
        self.repository = Repository()

    def create(self, obj: Category):
        self.repository.create(f'{FILE_LOCATION}{FILE_CATEGORY_NAME}', obj)

    def read(self):
        return self.repository.find_all(f'{FILE_LOCATION}{FILE_AUTHOR_NAME}')

    def update(self, obj: Category, key: str):
        self.repository.update(f'{FILE_LOCATION}{FILE_CATEGORY_NAME}', obj, key)

    def delete(self, key: str):
        self.repository.delete(f'{FILE_LOCATION}{FILE_CATEGORY_NAME}', key)


