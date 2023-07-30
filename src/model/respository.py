import json

from src.model.author import Author
from src.model.config import FILE_USER_NAME, FILE_LOCATION, FILE_ENCODING, \
    FILE_AUTHOR_NAME, IDENTIFIER


class Repository:

    def create(self, file_path: str, obj):
        file_content = self.find_all(file_path)
        with open(file_path, 'w+', encoding=FILE_ENCODING) as f:
            f.seek(0)
            file_content.append(obj.__repr__())
            json.dumps(file_content, indent=4)
            f.seek(0)
            json.dump(file_content, f)

    def update(self, file_path: str, obj_new, key: str):
        file_content = self.find_all(file_path)
        for idx, obj in enumerate(file_content):
            if obj[IDENTIFIER] == key:
                file_content[idx] = obj_new.__repr__()
        self.save_all(file_path, file_content)

    def delete(self, file_path: str, key: str):
        file_content = self.find_all(file_path)
        for idx, obj in enumerate(file_content):
            if obj[IDENTIFIER] == key:
                del file_content[idx]
        self.save_all(file_path, file_content)

    def find_all(self, file_path: str):
        with open(file_path, 'r', encoding=FILE_ENCODING) as f:
            return json.load(f)

    def find_limit(self, file_path: str, limit: int, priority: str):
        lst = []
        all_objs = self.find_all(file_path)
        for obj in all_objs:
            if obj['priority'].lower() == priority.lower():
                print('tak')
                lst.append(obj)
            if limit == len(lst):
                break

        return lst

    def save_all(self, file_path: str, objects: list[Author]):
        with open(file_path, 'w+', encoding=FILE_ENCODING) as f:
            f.seek(0)
            file_content = objects
            json.dumps(file_content, indent=4)
            f.seek(0)
            json.dump(file_content, f)
