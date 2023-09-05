from datetime import datetime
from src.model.category import Category
from src.model.generator import Generator
from src.model.user import User
from src.service.status_service import StatusService


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
        self.status_opt = StatusService()
        self.status = None
        self.comments = None
        self.roadmap = None
        self.attachments = None

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
            'status': self.status,
            'roadmap': self.roadmap

        }

    @staticmethod
    def actual_date():
        return datetime.now()

