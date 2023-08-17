import json
from ast import literal_eval
import requests

from src.model.config import FILE_LOCATION, FILE_QUESTION, FILE_ROADMAP


class JsonFromService:

    def __init__(self):
        self.link = 'http://89.74.210.195:8090/jfs-cloud-app-ci/v1/api/storage/'
        self.headers = {'Tenant-Id': 'My-CRM'}

    def get_objects_with_parametrization(self, name_file: str, type_s: str,
                                         parametrization: str):
        response = requests.get(f'{self.link}{type_s}?filename={name_file}',
                                headers=self.headers)
        response_con = literal_eval(response.content.decode('utf-8'))
        return [obj for obj in response_con if parametrization in obj.values()]

