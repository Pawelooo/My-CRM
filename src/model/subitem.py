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
        self.level = 0
        self.status = None
        self.update_status()
        self.comments = None

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

    def update_status(self):
        obj = list(self.status_opt.read()[0].values())
        self.status = obj[self.level]
        if not self.level >= len(obj) - 1:
            self.level += 1

