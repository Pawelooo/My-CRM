from collections import Counter

from src.model.generator import Generator
from src.service.jfs import JsonFromService
from src.service.subitem_service import SubItemService
from src.service.tags.tag import Tag


class SubItem:

    def __init__(self, name: str, title: str, description: str, name_file, tag: Tag):
        self.id = Generator().generate_number()
        self.name = name
        self.title = title
        self.description = description
        self.id_item = []
        self.opened_by = None
        self.deadline = None
        self.done = False
        self.name_file = name_file
        self.attachments = JsonFromService().add_file(self.name_file,
                                                      'upload/')
        self.status = None
        self.comments = None
        self.roadmap = None
        self.tag = tag

    def __repr__(self):
        return {
            'id': self.id,
            'name': self.name,
            'title': self.title,
            'description': self.description,
            'id_item': self.id_item,
            'opened by': self.opened_by,
            'deadline': self.deadline,
            'done': self.done,
            'status': self.status,
            'name_file': self.name_file,
            'attachments': self.attachments,
            'tag': self.tag,
        }

    def amount_tag_items(self):
        subitem = SubItemService().read()
        cnt = Counter()
        for obj in subitem:
            if obj['roadmap'].id == self.id:
                for key, value in obj.items():
                    if key == "tag":
                        cnt[value] += 1
        return dict(cnt)
