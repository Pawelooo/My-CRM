
from src.model.book import Book
from src.model.config import FILE_LOCATION, FILE_BOOK_NAME, FILE_AUTHOR_NAME
from src.model.respository import Repository


class BookService:

    def __init__(self):
        self.repository = Repository()

    def create(self, obj: Book):
        self.repository.create(f'{FILE_LOCATION}{FILE_BOOK_NAME}', obj)

    def read_book(self):
        return self.repository.find_all(f'{FILE_LOCATION}{FILE_AUTHOR_NAME}')

    def update(self, obj: Book, key: str):
        self.repository.update(f'{FILE_LOCATION}{FILE_BOOK_NAME}', obj, key)

    def delete(self, key: str):
        self.repository.delete(f'{FILE_LOCATION}{FILE_BOOK_NAME}', key)


