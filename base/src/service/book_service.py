
from src.model.book import Book
from src.model.config import FILE_LOCATION, FILE_BOOK_NAME, FILE_AUTHOR_NAME
from src.model.respository import Repository
from src.service.validators.book_validator import BookValidator


class BookService:

    def __init__(self):
        self.repository = Repository()
        self.validator = BookValidator()

    def create(self, obj: Book):
        self.validator.validate(obj.__repr__(), 'create')
        self.repository.create(f'{FILE_LOCATION}{FILE_BOOK_NAME}', obj)

    def read_book(self):
        return self.repository.find_all(f'{FILE_LOCATION}{FILE_AUTHOR_NAME}')

    def update(self, obj: Book, key: str):
        self.validator.validate(obj.__repr__(), 'update')
        self.repository.update(f'{FILE_LOCATION}{FILE_BOOK_NAME}', obj, key)

    def delete(self, obj: Book, key: str):
        self.validator.validate(obj.__repr__(), 'delete')
        self.repository.delete(f'{FILE_LOCATION}{FILE_BOOK_NAME}', key)


