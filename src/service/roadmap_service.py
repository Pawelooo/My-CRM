import datetime

from src.model.roadmap import Roadmap
from src.model.config import FILE_LOCATION, FILE_ROADMAP
from src.model.respository import Repository


class RoadmapService:

    def __init__(self):
        self.repository = Repository()

    def create(self, obj: Roadmap):
        self.repository.create(f'{FILE_LOCATION}{FILE_ROADMAP}', obj)

    def update(self, obj: Roadmap, key: str):
        self.repository.update(f'{FILE_LOCATION}{FILE_ROADMAP}', obj, key)



