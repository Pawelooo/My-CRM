from datetime import datetime


class Roadmap:

    def __init__(self, type_item, title: str, priority, complexity,
                 goal_completion: datetime, added: datetime, user_id: int):
        self.type_item = type_item
        self.title = title
        self.priority = priority
        self.complexity = complexity
        self.goal_completion = goal_completion
        self.added = added
        self.user_id = user_id

    def __repr__(self):
        return {
            'type item': self.type_item,
            'title': self.title,
            'priority': self.priority,
            'complexity': self.complexity,
            'goal completion': self.goal_completion,
            'added': self.added,
            'user id': self.user_id
        }