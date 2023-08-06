from src.model.author import Author
from src.model.config import FILE_USER_NAME, FILE_LOCATION, FILE_AUTHOR_NAME
from src.model.respository import Repository
from src.service.validators.author_validator import AuthorValidator


class AuthorService:

    def __init__(self):
        self.repository = Repository()
        self.validator = AuthorValidator()

    def create(self, obj: Author):
        self.repository.create(f'{FILE_LOCATION}{FILE_AUTHOR_NAME}',
                               obj.__repr__())

    def update(self, obj: Author, key: str):
        self.validator.validate(obj.__repr__(), 'update')
        self.repository.update(f'{FILE_LOCATION}{FILE_AUTHOR_NAME}',
                               obj.__repr__(), key)

    def read(self):
        return self.repository.find_all(f'{FILE_LOCATION}{FILE_AUTHOR_NAME}')

    def delete(self, obj: Author, key: str):
        self.validator.validate(obj.__repr__(), 'delete')
        self.repository.delete(f'{FILE_LOCATION}{FILE_USER_NAME}', key)

