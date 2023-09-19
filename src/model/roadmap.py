from collections import Counter
from datetime import datetime
from typing import Self

from src.model.category import Category
from src.model.config import FORMAT_DATE
from src.model.generator import Generator
from src.model.item import Item
from src.model.user import User
from src.service.item_service import ItemService
from src.service.tags.tag import Tag


class Roadmap:

    def __init__(self, type_item,  title: str, priority, complexity,
                 goal_completion: datetime, added: datetime, user_id: int):
        self.id = Generator().generate_number()
        self.type_item = type_item
        self.title = title
        self.priority = priority
        self.complexity = complexity
        self.goal_completion = goal_completion
        self.added = added
        self.user_id = user_id
        self.item = []

    def __repr__(self):
        return str({
            "type_item": f"{self.type_item}",
            "title": f"{self.title}",
            "priority": f"{self.priority}",
            "complexity": f"{self.complexity}",
            "goal_completion": f"{self.goal_completion.strftime(FORMAT_DATE)}",
            "added": f"{self.added.strftime('%d.%m.%Y')}",
            "user_id": f"{self.user_id}",
            "id": f"{self.id}"
        })

    def amount_items(self):
        item = ItemService().read()
        cnt = Counter()
        for obj in item:
            if obj['roadmap'].id == self.id:
                for key, value in obj.items():
                    if key == "status":
                        cnt[value] += 1
        return dict(cnt)
