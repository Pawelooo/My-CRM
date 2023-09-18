from datetime import datetime
from src.model.config import FORMAT_DATE
from src.model.generator import Generator
from src.model.item import Item


class Roadmap:

    def __init__(self, type_item,  title: str, priority, complexity,
                 goal_completion: datetime, added: datetime, user_id: int,
                 sub_item: Item):
        self.id = Generator().generate_number()
        self.type_item = type_item
        self.title = title
        self.priority = priority
        self.complexity = complexity
        self.goal_completion = goal_completion
        self.added = added
        self.user_id = user_id
        self.sub_item = sub_item

    def __repr__(self):
        return {
            'type_item': self.type_item,
            'title': self.title,
            'priority': self.priority,
            'complexity': self.complexity,
            'goal_completion': self.goal_completion.strftime(FORMAT_DATE),
            'added': self.added.strftime('%d.%m.%Y'),
            'user_id': self.user_id,
            'item': self.sub_item,
            'id': self.id
        }

    def update_status_item(self):
        self.sub_item.update_status()
