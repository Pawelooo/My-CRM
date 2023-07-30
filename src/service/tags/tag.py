import json

from src.model.config import FILE_ENCODING, FILE_TAG, FILE_LOCATION_TAG


class Tag:
    def __init__(self):
        self.values = []  # the db should be updated accordingly

    def find_all(self):
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
        self.values.append(value)  # the db should be updated accordingly
        self.save()
        return self.get(value)

    def get_all(self):
        with open(f'{FILE_LOCATION_TAG}{FILE_TAG}', 'r+',
                  encoding=FILE_ENCODING) as f:
            self.values = json.load(f)

    def save(self):
        with open(f'{FILE_LOCATION_TAG}{FILE_TAG}', 'w+',
                  encoding=FILE_ENCODING) as file:
            json.dump(self.values, file)

