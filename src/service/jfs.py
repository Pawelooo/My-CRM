import json
from ast import literal_eval
import requests

from src.model.config import FILE_LOCATION, INT_JFSCF_TENANT_NAME, \
    INT_JFSCF_URL


class JsonFromService:

    def __init__(self):
        self.link = INT_JFSCF_URL
        self.headers = {'Tenant-Id': INT_JFSCF_TENANT_NAME}

    def add_file(self, name_file: str, type_s: str):
        files = {'file': open(f'{FILE_LOCATION}{name_file}', 'rb')}
        return requests.post(f'{self.link}{type_s}', headers=self.headers,
                             files=files).status_code

    def update_file(self, name_file: str, type_s: str):
        files = {'file': open(f'{FILE_LOCATION}{name_file}', 'rb')}
        return requests.post(f'{self.link}{type_s}', headers=self.headers,
                             files=files).status_code

    def read_file(self, name_file: str, type_s: str):
        response = requests.get(
            f'{self.link}{type_s}?filename={name_file}',
            headers=self.headers)
        response_d = literal_eval(response.content.decode('utf-8'))
        with open(f'{FILE_LOCATION}{name_file}', 'w',
                  encoding='utf-8') as file:
            json.dump(response_d, file)
        return response_d

    def get_objects_with_parametrization(self, name_file: str, type_s: str,
                                         parametrization: str):
        response = requests.get(f'{self.link}{type_s}?filename={name_file}',
                                headers=self.headers)
        response_con = literal_eval(response.content.decode('utf-8'))
        return [obj for obj in response_con if parametrization in obj.values()]
