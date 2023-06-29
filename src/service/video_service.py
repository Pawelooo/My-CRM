from datetime import datetime

from src.model.author import Author
from src.model.category import Category
from src.model.video import Video


class VideoService:

    def __init__(self):
        self.video = None

    def create_video(self, name: str, category: Category, author: Author, link: str = None,
                     topic: str = None, version: str = None, date_publication: datetime = None):
        self.video = Video(name, category, author, link, topic, version, date_publication)

    def read_video(self):
        return f'Name: {self.video.name}, Category: {self.video.category}, Author: {self.video.author}, ' \
               f'Link: {self.video.link}, Topic: {self.video.topic}, Version: {self.video.version},' \
               f'Date publication: {self.video.date_publication}'

    def update_video(self, key: str, new_value: str):
        video = vars(self.video)
        video[key] = new_value

    def delete_video(self):
        del self.video


