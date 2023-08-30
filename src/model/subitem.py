from src.service.roadmap_service import RoadmapService
from src.service.status_service import StatusService


class SubItem:

    def __init__(self):
        self.roadmap_item = None
        self.roadmap = RoadmapService()

    def get_repository(self, id_roadmap: int):
        for obj in self.roadmap.read():
            if obj['id'] == id_roadmap:
                self.roadmap_item = obj
