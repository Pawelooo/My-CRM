from src.service.tags.tag import Tag


class SubItem:

    def __init__(self, tag: Tag):
        self.tag = tag

    def __repr__(self):
        return {
            'tag': self.tag
        }

