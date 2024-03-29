import json

from base.src.model.config import FILE_ENCODING, FILE_LOCATION_TAG, WRITE_PLUS, \
    READ_PLUS


class Tag:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.values = []

    def find_all(self):
        self.get_all()
        return self.values

    def get(self, value):
        self.get_all()
        it = iter(self.values)
        while True:
            try:
                element = next(it)
                if element.lower() == value.lower():
                    return element
            except StopIteration:
                break
        self.values.append(value)
        self.save()
        return self.get(value)

    def get_all(self):
        with open(f'{FILE_LOCATION_TAG}{self.file_name}', READ_PLUS,
                  encoding=FILE_ENCODING) as f:
            self.values = json.load(f)

    def save(self):
        with open(f'{FILE_LOCATION_TAG}{self.file_name}', WRITE_PLUS,
                  encoding=FILE_ENCODING) as file:
            json.dump(self.values, file)


