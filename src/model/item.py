from datetime import datetime
from typing import List, Any

from src.model.category import Category
from src.model.config import FILE_ITEM, GET_FILE, UPLOAD_FILE, FILE_SUBITEM, \
    FILE_STATUS_NAME, CUSTOM_STATUS

from src.model.generator import Generator
from src.model.subitem import SubItem
from src.model.user import User
from src.service.jfs import JsonFromService
from src.service.tags.tag import Tag
from src.view.view import View


class Item:

    def __init__(self, name: str, title: str, description: str, name_file: str,
                 deadline: datetime, category: Category, assignee: User,
                 tag: Tag):
        self.id = Generator().generate_number()
        self.name = name
        self.title = title
        self.description = description
        self.deadline = deadline
        self.category = category
        self.opened_by = self.actual_date()
        self.assignee = assignee
        self.name_file = name_file
        self.attachments = JsonFromService().add_file(self.name_file,
                                                      UPLOAD_FILE)
        self.status_opt = JsonFromService().read_file(FILE_ITEM, GET_FILE)
        self.subitems = JsonFromService().read_file(FILE_SUBITEM, GET_FILE)
        self.sub_item = [12, 15, 17, 18]
        self.comments = None
        self.roadmap = None
        self.tag = tag
        self.status = JsonFromService().read_file(FILE_STATUS_NAME, GET_FILE)
        self.jfs = JsonFromService()
        self.current_status = 0
        self.custom_status = None


    def __repr__(self):
        return {
            'id': self.id,
            'name': self.name,
            'title': self.title,
            'description': self.description,
            'opened_by': self.opened_by,
            'deadline': self.deadline,
            'category': self.category,
            'assignee': self.assignee,
            'status': self.status,
            'name_file': self.name_file,
            'attachments': self.attachments,
            'roadmap': self.roadmap,
            'tag': self.tag,
            'custom_status': self.custom_status,
        }

    @staticmethod
    def actual_date():
        return datetime.now()

    def update_status(self):
        self.status = self.get_next_status()
        self.jfs.update_file(self.name_file, UPLOAD_FILE)

    def get_next_status(self):
        if self.current_status <= len(self.status) - 1:
            self.current_status += 1
        return self.status[self.current_status]

    def check_status(self):
        if all(obj['status'] == 'DONE' for obj in self.subitems):
            self.update_status()
        if any(obj['status'] == 'INPROGRESS' for obj in self.subitems):
            self.update_status()

    def add_sub_item(self, id_subitem):
        self.sub_item.append(id_subitem)

    def move_status(self):
        if self.status == 'INPROGRESS' and any([subitem['status'].__eq__('DONE') for subitem in self.subitems]):
            for subitem in self.subitems:
                if subitem['id'] in self.sub_item:
                    subitem['status'] = 'DONE'
            self.update_status()

    def get_custom_status(self):
        v1 = View()
        result = v1.get_attribute(CUSTOM_STATUS)
        self.custom_status = result

