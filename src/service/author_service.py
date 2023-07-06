from src.model.author import Author
from src.model.config import FILE_USER_NAME, FILE_LOCATION, FILE_AUTHOR_NAME
from src.model.respository import Repository


class AuthorService:

    def __init__(self):
        self.repository = Repository()

    def create(self, obj: Author):
        self.repository.create(f'{FILE_LOCATION}{FILE_AUTHOR_NAME}', obj)

    def update(self, obj: Author, key: str):
        self.repository.update(f'{FILE_LOCATION}{FILE_AUTHOR_NAME}', obj, key)

    def read(self):
        return self.repository.find_all(f'{FILE_LOCATION}{FILE_AUTHOR_NAME}')

    def delete(self, key: str):
        self.repository.delete(f'{FILE_LOCATION}{FILE_USER_NAME}', key)

