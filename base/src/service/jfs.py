import json

from base.src.model.config import FILE_LOCATION, INT_JFSCF_URL, \
    INT_JFSCF_TENANT_NAME, FILE_ENCODING, SIZE_IMAGE, FOLDER_IMAGES, \
    QUALITY_IMAGE, DOWNLOAD
from base.src.service.validators.jfs_validation import JfsValidator
from PIL import Image

import os
import shutil
import zipfile
from ast import literal_eval
from typing import List, Dict

import requests

from base.src.model.config import FILE_ZIP, FILES_ZIPPED, FILES_DOWNLOAD_ALL, \
    GET_FILE


class JsonFromService:

    def __init__(self):
        self.link = INT_JFSCF_URL
        self.headers = {'Tenant-Id': INT_JFSCF_TENANT_NAME}
        self.validation = JfsValidator()

    def add_file(self, name_file: str, type_s: str, location: str):
        files = {'file': open(f'{location}{name_file}', 'r')}
        res = requests.post(f'{self.link}{type_s}', headers=self.headers,
                            files=files)
        return res.status_code if (result := self.validation.validate(
            res)) is None else result

    def update_file(self, name_file: str, type_s: str):
        files = {'file': open(f'{FILE_LOCATION}{name_file}', 'rb')}

        res = requests.post(f'{self.link}{type_s}', headers=self.headers,
                            files=files)
        return res.status_code if (result := self.validation.validate(
            res)) is None else result

    def read_file(self, name_file: str, type_s: str):
        response = requests.get(
            f'{self.link}{type_s}?filename={name_file}',
            headers=self.headers)
        if (res := self.validation.validate(response)) is None:
            response_d = literal_eval(response.content.decode(FILE_ENCODING))

            with open(f'{FILE_LOCATION}{name_file}', 'w',
                      encoding=FILE_ENCODING) as file:
                json.dump(response_d, file)
            return response_d
        return res

    def read_all_files(self, type_s):
        response = requests.get(f'{self.link}{type_s}', headers=self.headers)
        if (res := self.validation.validate(response)) is None:
            response_d = literal_eval(
                response.content.decode(FILE_ENCODING))
            return response_d
        return res

    def get_objects_with_parametrization(self, name_file: str, type_s: str,
                                         parametrization: str):
        response = requests.get(f'{self.link}{type_s}?filename={name_file}',
                                headers=self.headers)
        if (res := self.validation.validate(response)) is None:
            response_con = literal_eval(response.content.decode(FILE_ENCODING))
            return [obj for obj in response_con if
                    parametrization in obj.values()]
        return res

    def compress(self, place: str):
        images = self.get_images(place)
        os.makedirs(place, exist_ok=True)
        for image in images:
            image_n = Image.open(f'{place}/{image}')
            image_n.thumbnail((SIZE_IMAGE, SIZE_IMAGE))
            image_n.save(f'{place}{image}', quality=QUALITY_IMAGE,
                         progressive=True)

    def get_images(self, place):
        images = []
        for file in os.listdir(place):
            path = os.path.join(place, file)
            if not os.path.isdir(path):
                images.append(file)
        return images

    def get_all_links(self):
        response = requests.get(f'{self.link}{FILES_DOWNLOAD_ALL}',
                                headers=self.headers)
        response_d = literal_eval(response.content.decode(FILE_ENCODING))
        return [obj for obj in response_d if obj['name'].startswith('db_')]

    def get_object(self, name_file: str):
        return literal_eval(
            requests.get(f'{self.link}{GET_FILE}?filename={name_file}',
                         headers=self.headers).content.decode(FILE_ENCODING))

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

    def get_object_from_cloud(self, name_file: str):
        return literal_eval(
            requests.get(f'{self.link}{DOWNLOAD}?filename={name_file}',
                         headers=self.headers).content.decode(FILE_ENCODING))

    def save_image(self, image):
        destination = os.path.join('../base/img/', image.filename)
        image.save(destination)
