from src.model.generator import Generator
from src.service.status_service import StatusService


class SubItem:

    def __init__(self, name: str, title: str, description: str):
        self.id = Generator().generate_number()
        self.name = name
        self.title = title
        self.description = description
        self.id_item = []
        self.opened_by = None
        self.deadline = None
        self.done = False
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
            'id item': self.id_item,
            'opened by': self.opened_by,
            'deadline': self.deadline,
            'done': self.done,
            'status': self.status
        }


