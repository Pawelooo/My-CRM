import json

from base.src.model.author import Author
from base.src.model.config import FILE_ENCODING, \
    IDENTIFIER, PRIORITY, WRITE_PLUS, READ


class Repository:

    def create(self, file_path: str, obj):
        file_content = self.find_all(file_path)
        file_content.append(obj.__repr__())
        with open(file_path, 'w', encoding=FILE_ENCODING) as f:
            json.dump(file_content, f, indent=4, separators=(',', ': '))

    def update(self, file_path: str, obj_new, key: str):
        file_content = self.find_all(file_path)
        self.save_all(file_path, [obj_new.__repr__() if obj[IDENTIFIER] == key
                                  else obj for idx, obj in
                                  enumerate(file_content)])

    def delete(self, file_path: str, key: str):
        file_content = self.find_all(file_path)
        self.save_all(file_path,
                      [obj for idx, obj in enumerate(file_content)
                       if obj[IDENTIFIER] != key])

    def find_all(self, file_path: str):
        with open(file_path, READ, encoding=FILE_ENCODING) as f:
            try:
                return json.load(f)
            except:
                return []

    def find_limit(self, file_path: str, limit: int, priority: str):
        return list(filter(lambda x: (x[PRIORITY].lower() == priority
                                      or x[PRIORITY] is not None),
                           self.find_all(file_path)))[:limit]

    def save_all(self, file_path: str, objects: list[Author]):
        with open(file_path, WRITE_PLUS, encoding=FILE_ENCODING) as f:
            f.seek(0)
            file_content = objects
            json.dumps(file_content, indent=4)
            f.seek(0)
            json.dump(file_content, f)
