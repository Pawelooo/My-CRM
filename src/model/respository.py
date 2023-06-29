import json

from src.model.author import Author


class Repository:

    def save_to_file(self, name_file: str, obj):
        data = self.check_is_exist(name_file)
        print(data)
        with open(f'../../resources/data/{name_file}', 'r+', encoding='utf-8') as f:
            file_content = json.load(f)
            file_content['data'].append(obj)
            file_content = json.dumps(set(file_content))
            f.seek(0)
            json.dump(file_content, f)

    def check_is_exist(self, name_file: str):
        try:
            with open(f'../../resources/data/{name_file}', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError as ex:
            print(f'This file is not exist, {ex}')
            with open(f'../../resources/data/{name_file}', 'w', encoding='utf-8') as f:
                json.dump({}, f)


def main() -> None:
    r = Repository()
    r.save_to_file('new.json', Author('Pawel', 'gaga', 'gagafg', 'gag').reprisend_to_json())


if __name__ == '__main__':
    main()
