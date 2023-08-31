from datetime import datetime
from src.model.category import Category
from src.model.generator import Generator
from src.model.user import User
from src.service.tags.tag import Tag


class Item:

    def __init__(self, name: str, title: str, description: str,
                 deadline: datetime, category: Category, assignee: User,
                 tag: Tag):
        self.id = Generator().generate_number()
        self.name = name
        self.title = title
        self.description = description
        self.deadline = deadline
        self.category = category
        self.opened_by = self.actual_date()
        self.assignee = assignee
        self.tag = tag


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
            'tag': self.tag
        }

    @staticmethod
    def actual_date():
        return datetime.now()
