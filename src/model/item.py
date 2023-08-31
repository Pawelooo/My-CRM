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
        self.level = 0
        self.status = None
        self.update_status()

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
            'status': self.status
        }

    @staticmethod
    def actual_date():
        return datetime.now()

    def update_status(self):
        obj = list(self.status_opt.read()[0].values())
        self.status = obj[self.level]
        if not self.level >= len(obj) - 1:
            self.level += 1
