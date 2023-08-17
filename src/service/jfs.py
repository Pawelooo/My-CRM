import json
from ast import literal_eval
import requests

from src.model.config import FILE_LOCATION, FILE_QUESTION, FILE_ROADMAP


class JsonFromService:

    def __init__(self):
        self.link = 'http://89.74.210.195:8090/jfs-cloud-app-ci/v1/api/storage/'
        self.headers = {'Tenant-Id': 'My-CRM'}

    def add_file(self, name_file: str, type_s: str):
        files = {'file': open(f'{FILE_LOCATION}{name_file}', 'rb')}
        return requests.post(f'{self.link}{type_s}', headers=self.headers, files=files).status_code

    def update_file(self, name_file: str, type_s: str):
        files = {'file': open(f'{FILE_LOCATION}{name_file}', 'rb')}
        return requests.post(f'{self.link}{type_s}', headers=self.headers, files=files).status_code

    def read_file(self, name_file: str, type_s: str):
        response = requests.get(f'{self.link}{type_s}?filename={name_file}', headers=self.headers)
        response_d = literal_eval(response.content.decode('utf-8'))
        with open(f'{FILE_LOCATION}{name_file}', 'w') as file:
            json.dump(response_d, file)
        return response_d
