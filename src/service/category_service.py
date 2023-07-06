from src.model.category import Category
from src.model.config import FILE_LOCATION, FILE_CATEGORY_NAME
from src.model.respository import Repository


class CategoryService:

    def __init__(self):
        self.repository = Repository()

    def create(self, obj: Category):
        self.repository.create(f'{FILE_LOCATION}{FILE_CATEGORY_NAME}', obj)

    def read(self, file_path: str):
        return self.repository.find_all(file_path)

    def update(self, obj: Category, key: str):
        self.repository.update(f'{FILE_LOCATION}{FILE_CATEGORY_NAME}', obj, key)

    def delete(self, key: str):
        self.repository.delete(f'{FILE_LOCATION}{FILE_CATEGORY_NAME}', key)

