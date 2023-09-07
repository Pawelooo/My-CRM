from src.model.config import FILE_SUBITEM
from src.model.generator import Generator
from src.service.jfs import JsonFromService
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
        self.status_opt = JsonFromService().read_file(FILE_SUBITEM, 'upload/')
        self.level = 0
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

    def update_status(self):
        obj = list(self.status_opt.read()[0].values())
        self.status = obj[self.level]
        if not self.level >= len(obj) - 1:
            self.level += 1
