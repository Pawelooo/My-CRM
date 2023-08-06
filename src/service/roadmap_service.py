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

    def read(self):
        return self.repository.find_all(f'{FILE_LOCATION}{FILE_ROADMAP}')

    def read_limit(self, limit: int, priority):
        return self.repository.find_limit(f'{FILE_LOCATION}{FILE_ROADMAP}',
                                          limit, priority)

    def delete(self, key: str):
        self.repository.delete(f'{FILE_LOCATION}{FILE_ROADMAP}', key)
