from datetime import datetime
from src.model.category import Category
from src.model.generator import Generator
from src.model.user import User
from src.service.jfs import JsonFromService
from src.service.tags.tag import Tag


class Item:

    def __init__(self, name: str, title: str, description: str, name_file: str,
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
        self.name_file = name_file
        self.attachments = JsonFromService().add_file(self.name_file,
                                                      'upload/')
        self.status = None
        self.comments = None
        self.roadmap = None
        self.tag = tag
        self.status = 'TODO'

    def __repr__(self):
        return str({
            'id': f'{self.id}',
            'name': f'{self.name}',
            'title': f"{self.title}",
            'description': f'{self.description}',
            'opened_by': f'{self.opened_by}',
            'deadline': f"{self.deadline}",
            'category': f'{self.category}',
            'assignee': f'{self.assignee}',
            'status': f"{self.status}",
            'name_file': f'{self.name_file}',
            'attachments': f'{self.attachments}',
            'roadmap': f'{self.roadmap}',
            'tag': f"{self.tag}",
        })


    @staticmethod
    def actual_date():
        return datetime.now()
