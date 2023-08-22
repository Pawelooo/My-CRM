
import json
import requests

from ast import literal_eval
from src.model.config import FILE_LOCATION, INT_JFSCF_URL, \
    INT_JFSCF_TENANT_NAME, FILE_ENCODING, SIZE_IMAGE, FOLDER_IMAGES, \
    QUALITY_IMAGE
from src.service.validators.jfs_validation import JfsValidator
from PIL import Image
import os



class JsonFromService:

    def __init__(self):

        self.link = INT_JFSCF_URL
        self.headers = {'Tenant-Id': INT_JFSCF_TENANT_NAME}
        self.validation = JfsValidator()

    def add_file(self, name_file: str, type_s: str):
        files = {'file': open(f'{FILE_LOCATION}{name_file}', 'rb')}
        res = requests.post(f'{self.link}{type_s}', headers=self.headers,
                            files=files)
        if (result := self.validation.validate(res)) is None:
            return res.status_code
        return result

    def update_file(self, name_file: str, type_s: str):
        files = {'file': open(f'{FILE_LOCATION}{name_file}', 'rb')}
        res = requests.post(f'{self.link}{type_s}', headers=self.headers,
                            files=files)
        if (result := self.validation.validate(res)) is None:
            return res.status_code
        return result

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

    def get_objects_with_parametrization(self, name_file: str, type_s: str,
                                         parametrization: str):
        response = requests.get(f'{self.link}{type_s}?filename={name_file}',
                                headers=self.headers)
        if (res := self.validation.validate(response)) is None:
            response_con = literal_eval(response.content.decode(FILE_ENCODING))
            return [obj for obj in response_con if
                    parametrization in obj.values()]
        return res

    def compress(self):
        images = self.get_images()
        os.makedirs(FOLDER_IMAGES, exist_ok=True)
        for image in images:
            image_n = Image.open(f'{FOLDER_IMAGES}/{image}')
            image_n.thumbnail((SIZE_IMAGE, SIZE_IMAGE))
            image_n.save(f'{FOLDER_IMAGES}{image}', quality=QUALITY_IMAGE, progressive=True)


    def get_images(self):
        images = []
        for file in os.listdir(FOLDER_IMAGES):
            path = os.path.join(FOLDER_IMAGES, file)
            if os.path.isdir(path):
                continue
            images.append(file)
        return images


