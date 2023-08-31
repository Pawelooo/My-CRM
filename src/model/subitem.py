from src.service.roadmap_service import RoadmapService
from src.service.status_service import StatusService


class SubItem:

    def __init__(self):
        self.roadmap_item = None
        self.roadmap = RoadmapService()

    def get_repository(self, id_roadmap: int):
        obj = iter(self.roadmap.read())
        while True:
            try:
                element = next(obj)
            except StopIteration:
                break
            else:
                if element['id'] == id_roadmap:
                    return element

