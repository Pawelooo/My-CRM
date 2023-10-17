from collections import Counter
from datetime import datetime
from base.src.model.config import MESSAGE_TO_USER, DATE

from base.src.view.view import View
from base.src.model.config import FORMAT_DATE
from base.src.model.generator import Generator
from base.src.service.item_service import ItemService


class Roadmap:

    def __init__(self, type_item: str, title: str, priority, complexity: str,
                 goal_completion: datetime, added: datetime, user_id: int,
                 deadline_date: datetime):
        self.id = Generator().generate_number()
        self.type_item = type_item
        self.title = title
        self.priority = priority
        self.complexity = complexity
        self.goal_completion = goal_completion
        self.added = added
        self.user_id = user_id
        self.deadline_date = deadline_date
        self.subitem = []
        self.item = []

    def __repr__(self):
        return {
            "type_item": f"{self.type_item}",
            "title": f"{self.title}",
            "priority": f"{self.priority}",
            "complexity": f"{self.complexity}",
            "goal_completion": f"{self.goal_completion.strftime(FORMAT_DATE)}",
            "added": f"{self.added.strftime('%d.%m.%Y')}",
            "user_id": f"{self.user_id}",
            "id": f"{self.id}"
        }

    def set_deadline_date(self):
        v1 = View()
        result = v1.get_attribute(MESSAGE_TO_USER)
        self.deadline_date = datetime.strptime(result, DATE)

    def update_item_status(self):
        self.item.update_status()

    def update_status_subitem(self):
        self.subitem.update_status()

    def amount_items(self):
        item = ItemService().read()
        cnt = Counter()
        for obj in item:
            if obj['roadmap'].id == self.id:
                for key, value in obj.items():
                    if key == "status":
                        cnt[value] += 1
        return dict(cnt)
