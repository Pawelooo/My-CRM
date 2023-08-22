import json
from ast import literal_eval
import requests

from src.model.config import FILE_LOCATION, INT_JFSCF_URL, INT_JFSCF_TENANT_NAME
from src.service.validators.jfs_validation import JfsValidator


class JsonFromService:

    def __init__(self):
        self.link = INT_JFSCF_URL
        self.headers = {'Tenant-Id': INT_JFSCF_TENANT_NAME}
        self.validation = JfsValidator()

    def add_file(self, name_file: str, type_s: str):
        files = {'file': open(f'{FILE_LOCATION}{name_file}', 'rb')}
        res = requests.post(f'{self.link}{type_s}',headers=self.headers,
                             files=files)
        result = self.validation.validate(res)
        if result:
            return result
        return res.status_code

    def update_file(self, name_file: str, type_s: str):
        files = {'file': open(f'{FILE_LOCATION}{name_file}', 'rb')}
        res = requests.post(f'{self.link}{type_s}', headers=self.headers,
                             files=files)
        result = self.validation.validate(res)
        if result:
            return result
        return res.status_code

    def read_file(self, name_file: str, type_s: str):
        response = requests.get(
            f'{self.link}{type_s}?filename={name_file}',
            headers=self.headers)
        result = self.validation.validate(response)
        if result:
            return result
        response_d = literal_eval(response.content.decode('utf-8'))
        with open(f'{FILE_LOCATION}{name_file}', 'w',
                  encoding='utf-8') as file:
            json.dump(response_d, file)
        return response_d

    def get_objects_with_parametrization(self, name_file: str, type_s: str,
                                         parametrization: str):
        response = requests.get(f'{self.link}{type_s}?filename={name_file}',
                                headers=self.headers)
        result = self.validation.validate(response)
        if result:
            return result
        response_con = literal_eval(response.content.decode('utf-8'))
        return [obj for obj in response_con if parametrization in obj.values()]

def main() ->None:
    j1 = JsonFromService()
    # print(j1.add_file('db_author.json', 'upload'))
    print(j1.update_file('db_author.json', 'upload'))

if __name__ == '__main__':
    main()