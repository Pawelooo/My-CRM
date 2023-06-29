from src.model.author import Author


class AuthorService:

    def __init__(self):
        self.author = None

    def create_author(self, name: str, surname: str, website: str = None, country: str = None, topic: str = None):
        self.author = Author(name, surname, website, country, topic)

    def read_author(self):
        return f'Name: {self.author.name}, Surname: {self.author.surname}, Website: {self.author.website}, ' \
               f'Country: {self.author.country}, Topic: {self.author.topic}'

    def update_author(self, key: str, new_value: str):
        author = vars(self.author)
        author[key] = new_value

    def delete_object(self):
        del self.author


