import json
import os
import shutil
import zipfile
from ast import literal_eval
from typing import List, Dict

import requests

from src.model.config import FILE_ZIP, FILES_ZIPPED, FILES_DOWNLOAD_ALL, \
    GET_FILE


class JsonFromService:

    def __init__(self):
        self.link = 'http://89.74.210.195:8090/jfs-cloud-app-ci/v1/api/storage/'
        self.headers = {'Tenant-Id': 'My-CRM'}

    def get_all_links(self):
        response = requests.get(f'{self.link}{FILES_DOWNLOAD_ALL}',
                                headers=self.headers)
        response_d = literal_eval(response.content.decode('utf-8'))
        return [obj for obj in response_d if obj['name'].startswith('db_')]

    def get_object(self, name_file: str):
        response = requests.get(f'{self.link}{GET_FILE}?filename={name_file}',
                                headers=self.headers)
        response_d = literal_eval(response.content.decode('utf-8'))
        return response_d

    def get_all_files(self, name_files: List[Dict[str, str]]):
        if not os.path.exists(FILE_ZIP):
            os.makedirs(FILE_ZIP)
        for obj in name_files:
            with open(f'{FILE_ZIP}{obj["name"]}', 'w+', ) as f:
                json.dump(self.get_object(obj['name']), f)

    def pack_files(self, path_file: str):
        with zipfile.ZipFile(path_file, 'w') as zipf:
            for folder, _, files in os.walk(FILE_ZIP):
                for file in files:
                    path_file = os.path.join(folder, file)
                    name_zip = os.path.relpath(path_file, FILE_ZIP)
                    zipf.write(path_file, name_zip)
        shutil.rmtree(FILE_ZIP)

    def get_zipped_files(self, name_zip: str):
        all_links = self.get_all_links()
        self.get_all_files(all_links)
        self.pack_files(os.path.join(FILES_ZIPPED, name_zip))


