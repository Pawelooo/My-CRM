from base.src.model.author import Author
from base.src.model.config import FILE_USER_NAME, FILE_LOCATION, \
    FILE_AUTHOR_NAME, UPLOAD_FILE, GET_FILE
from base.src.model.respository import Repository
from base.src.service.jfs import JsonFromService
from base.src.service.validators.author_validator import AuthorValidator


class AuthorService:

    def __init__(self):
        self.repository = Repository()
        self.validator = AuthorValidator()

    def create(self, obj: Author):
        self.repository.create(f'{FILE_LOCATION}{FILE_AUTHOR_NAME}',
                               obj)

    def update(self, obj: Author, key: str):
        self.validator.validate(obj.__repr__(), 'update')
        self.repository.update(f'{FILE_LOCATION}{FILE_AUTHOR_NAME}',
                               obj, key)

    def read(self):
        return self.repository.find_all(f'{FILE_LOCATION}{FILE_AUTHOR_NAME}')

    def delete(self, obj: Author, key: str):
        self.validator.validate(obj.__repr__(), 'delete')
        self.repository.delete(f'{FILE_LOCATION}{FILE_USER_NAME}', key)


def main() -> None:
    AuthorService().create(
        Author('Paweł', 'test333', 'test33')
    )
    j1 = JsonFromService()
    j1.add_file(FILE_AUTHOR_NAME, UPLOAD_FILE)
    a = j1.read_file(FILE_AUTHOR_NAME, GET_FILE)
    print(a)

if __name__ == '__main__':
    main()
