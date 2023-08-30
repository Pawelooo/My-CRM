from datetime import datetime

from src.model.generator import Generator


class SubItem:

    def __init__(self, name: str, title: str, id_item: int, description: str):
        self.id = Generator().generate_number()
        self.name = name
        self.title = title
        self.description = description
        self.id_item = id_item
        self.opened_by = self.actual_date()
        self.deadline = None
        self.done = False

    def __repr__(self):
        return {
            'id': self.id,
            'name': self.name,
            'title': self.title,
            'description': self.description,
            'id item': self.id_item,
            'opened by': self.opened_by,
            'deadline': self.deadline,
            'done': self.done
        }

    @staticmethod
    def actual_date():
        return datetime.now()

    def update_done(self):
        self.done = True
        self.deadline = datetime.now()
