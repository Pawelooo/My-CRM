import datetime

from src.model.roadmap import Roadmap
from src.model.config import FILE_LOCATION, FILE_ROADMAP
from src.model.respository import Repository


class RoadmapService:

    def __init__(self):
        self.repository = Repository()










    def delete(self, key: str):
        self.repository.delete(f'{FILE_LOCATION}{FILE_ROADMAP}', key)
