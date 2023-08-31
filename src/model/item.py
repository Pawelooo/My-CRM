from datetime import datetime

from src.model.category import Category
from src.model.generator import Generator
from src.model.user import User
from src.service.roadmap_service import RoadmapService


class Item:

    def __init__(self, name: str, title: str, description: str,
                 deadline: datetime, category: Category, assignee: User):
        self.id = Generator().generate_number()
        self.name = name
        self.title = title
        self.description = description
        self.deadline = deadline
        self.category = category
        self.opened_by = self.actual_date()
        self.assignee = assignee
        self.roadmap_item = None
        self.roadmap = RoadmapService()

    def __repr__(self):
        return {
            'id': self.id,
            'name': self.name,
            'title': self.title,
            'description': self.description,
            'opened_by': self.opened_by,
            'deadline': self.deadline,
            'category': self.category,
            'assignee': self.assignee,
            'roadmap item': self.roadmap_item
        }

    @staticmethod
    def actual_date():
        return datetime.now()

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
