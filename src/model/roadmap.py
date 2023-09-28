from datetime import datetime
from src.model.config import FORMAT_DATE, MESSAGE_TO_USER
from src.model.generator import Generator
from src.model.item import Item
from src.view.view import View


class Roadmap:

    def __init__(self, type_item,  title: str, priority, complexity,
                 goal_completion: datetime, added: datetime, user_id: int,
                 deadline_date: datetime, item: Item):
        self.id = Generator().generate_number()
        self.type_item = type_item
        self.title = title
        self.priority = priority
        self.complexity = complexity
        self.goal_completion = goal_completion
        self.added = added
        self.user_id = user_id
        self.item = item
        self.deadline_date = deadline_date


    def __repr__(self):
        return {
            'type_item': self.type_item,
            'title': self.title,
            'priority': self.priority,
            'complexity': self.complexity,
            'goal_completion': self.goal_completion.strftime(FORMAT_DATE),
            'added': self.added.strftime('%d.%m.%Y'),
            'user_id': self.user_id,
            'item': self.item,
            'deadline date': self.deadline_date,
            'id': self.id
        }

    def set_deadline_date(self):
        v1 = View()
        result = v1.get_attribute(MESSAGE_TO_USER)
        self.deadline_date = datetime.strptime(result, '%d.%m.%Y')

    def update_item_status(self):
        self.item.update_status()
