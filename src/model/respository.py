import json

from src.model.author import Author
from src.model.config import FILE_USER_NAME, FILE_LOCATION, FILE_ENCODING, FILE_AUTHOR_NAME


class Repository:

    def __init__(self):
        pass
        # Czy powinnienem tutaj zdefinować zmienna klasową ?
        # self.file_content = self.get_all()

    def create(self, file_path: str, obj):
        file_content = self.get_all(file_path)
        with open(file_path, 'w+', encoding=FILE_ENCODING) as f:
            f.seek(0)
            file_content.append(obj.__repr__())
            json.dumps(file_content, indent=4)
            f.seek(0)
            json.dump(file_content, f)

    def update(self, file_path: str, obj_new, key: str):
        file_content = self.get_all(file_path)
        for idx, obj in enumerate(file_content):
            if obj['id'] == key:
                file_content[idx] = obj_new.__repr__()
        self.save_all(file_path, file_content)

    def delete(self, file_path: str, key: str):
        file_content = self.get_all(file_path)
        for idx, obj in enumerate(file_content):
            if obj['id'] == key:
                del file_content[idx]
        self.save_all(file_path, file_content)

    def find_all(self, file_path: str):
        with open(file_path, 'r', encoding=FILE_ENCODING) as f:
            return json.load(f)

    def get_all(self, file_path: str):
        with open(file_path, 'r', encoding=FILE_ENCODING) as f:
            return json.load(f)

    def save_all(self, file_path: str, objects: list[Author]):
        with open(file_path, 'w+', encoding=FILE_ENCODING) as f:
            f.seek(0)
            file_content = objects
            json.dumps(file_content, indent=4)
            f.seek(0)
            json.dump(file_content, f)


# def save_to_file(self, place_file: str, name_file: str, encode: str):
#     data = self.check_if_exist(FILE_LOCATION, FILE_USER_NAME, FILE_ENCODING)
#     print(data)
#     with open(f'{place_file}{name_file}', 'wr', encoding=encode) as f:
#         file_content = json.load(f)
#         file_content['data'].append(obj)
#         file_content = json.dumps(set(file_content))
#         f.seek(0)
#         json.dump(file_content, f)
#
# def check_if_exist(self, place_file: str, name_file: str, encode: str):
#     try:
#         with open(f'{place_file}{name_file}', 'r', encoding=encode) as f:
#             return json.load(f)
#     except FileNotFoundError as ex:
#         print(f'This file is not exist, {ex}')
#         with open(f'{place_file}{name_file}', 'w', encoding=encode) as f:
#             json.dump({}, f)
#
# def get_from_file(self, place_file: str, name_file: str, encode: str):
#     return self.check_if_exist(place_file, name_file, encode)


def main() -> None:
    r1 = Repository()
    # r1.create(f'{FILE_LOCATION}{FILE_AUTHOR_NAME}', Author('Paweł', 'Rutkowski', 'www.helion.com', "Poland"))
    # r1.create(f'{FILE_LOCATION}{FILE_AUTHOR_NAME}', Author('Patryk', 'Rutkowski', 'www.google.com', "Germany"))
    # r1.update(f'{FILE_LOCATION}{FILE_AUTHOR_NAME}', Author('Bartek', 'Nowa', 'www.google.com', "France "), '18')
    r1.delete(f'{FILE_LOCATION}{FILE_AUTHOR_NAME}', '18')


if __name__ == '__main__':
    main()
