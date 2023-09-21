from src.model.config import FILE_SUBITEM, FILE_STATUS_NAME, UPLOAD_FILE, \
    GET_FILE
from src.model.generator import Generator
from src.service.jfs import JsonFromService
from src.service.tags.tag import Tag


class SubItem:

    def __init__(self, name: str, title: str, description: str, name_file,
                 tag: Tag):
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
                                                      UPLOAD_FILE)
        self.status_opt = JsonFromService().read_file(FILE_STATUS_NAME,
                                                      GET_FILE)
        self.status = JsonFromService().read_file(FILE_STATUS_NAME, GET_FILE)
        self.comments = None
        self.roadmap = None
        self.tag = tag
        self.current_status = 0
        self.jfs = JsonFromService()

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
        self.status = self.get_next_status()
        self.jfs.update_file(self.name_file, UPLOAD_FILE)

    def get_next_status(self):
        if self.current_status <= len(self.status) - 1:
            self.current_status += 1
        return self.status[self.current_status]
