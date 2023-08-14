from PIL import Image
import os
from src.model.config import FOLDER_IMAGES, FOLDER_IMAGES_SAVE


class JsonFromService:

    def __init__(self):
        self.link = 'http://89.74.210.195:8090/jfs-cloud-app-ci/v1/api/storage/'
        self.headers = {'Tenant-Id': 'My-CRM'}

    def compress(self):
        images = self.get_images()
        os.makedirs(FOLDER_IMAGES_SAVE, exist_ok=True)
        for image in images:
            image_n = Image.open(f'{FOLDER_IMAGES}/{image}')
            image_n.thumbnail((200, 200))
            image_n.save(f'{FOLDER_IMAGES_SAVE}{image}', quality=85,
                         progressive=True)

    def get_images(self):
        images = []
        for file in os.listdir(FOLDER_IMAGES):
            path = os.path.join(FOLDER_IMAGES, file)
            if os.path.isdir(path):
                continue
            images.append(file)
        return images


