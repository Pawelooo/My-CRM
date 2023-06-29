from src.model.author import Author
from src.model.book import Book
from src.model.category import Category


class BookService:

    def __init__(self):
        self.book = None

    def create_book(self, name: str, category: Category, author: Author, link: str = None, topic: str = None,
                      version: str = None, page_count: str = None, date_publish: str = None):
        self.book = Book(name, category, author, link, topic, version, page_count, date_publish)

    def read_book(self):
        return f'Name: {self.book.name}, Category: {self.book.category}, Author: {self.book.author}, ' \
               f'Topic: {self.book.topic}, Version: {self.book.version}, Page Count: {self.book.page_count}, ' \
               f'Date publish: {self.book.date_publish}'

    def update_book(self, key: str, new_value: str):
        book = vars(self.book)
        book[key] = new_value

    def delete_book(self):
        del self.book


