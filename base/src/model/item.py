from collections import Counter
from datetime import datetime

from base.src.model.category import Category


from base.src.service.item_service import ItemService


from base.src.model.config import FILE_ITEM, GET_FILE, UPLOAD_FILE, \
    FILE_SUBITEM, \
    FILE_STATUS_NAME, CUSTOM_STATUS, INPROGRESS, STATUS, DONE, TODO, ID, \
    ROADMAP, TAG, FILE_LOCATION

from base.src.model.config import DONE
from base.src.model.config import TODO, UPLOAD
from base.src.model.generator import Generator
from base.src.model.user import User
from base.src.service.jfs import JsonFromService

from base.src.service.tags.tag import Tag
from base.src.view.view import View


class Item:

    def __init__(self, name: str, title: str, description: str, name_file: str,
                 deadline: datetime, category: Category, assignee: User,
                 tag: Tag, id_generate: str):
        self.id = id_generate
        self.name = name
        self.title = title
        self.description = description
        self.deadline = deadline
        self.category = category
        self.opened_by = self.actual_date()
        self.assignee = assignee
        self.name_file = name_file
        self.attachments = JsonFromService().add_file(self.name_file,
                                                      UPLOAD_FILE, FILE_LOCATION)
        self.status_opt = JsonFromService().read_file(FILE_ITEM, GET_FILE)
        self.subitems = JsonFromService().read_file(FILE_SUBITEM, GET_FILE)
        self.sub_item = []
        self.comments = None
        self.roadmap = None
        self.tag = tag
        self.current_status = 0
        self.status = JsonFromService().read_file(FILE_STATUS_NAME, GET_FILE)
        self.statuses = self.status[self.current_status]
        self.jfs = JsonFromService()
        self.custom_status = None
        self.status = None
        self.comments = None
        self.roadmap = None
        self.tag = tag
        self.status = TODO
        self.amounts = None
        self.amounts_tag = None

    def __repr__(self):
        return {
            'name': f'{self.name}',
            'title': f"{self.title}",
            'description': f'{self.description}',
            'opened_by': f'{self.opened_by}',
            'deadline': f"{self.deadline}",
            'category': f'{self.category}',
            'assignee': f'{self.assignee}',
            'status': f"{self.status}",
            'name_file': f'{self.name_file}',
            'attachments': f'{self.attachments}',
            'roadmap': f'{self.roadmap}',
            'tag': f"{self.tag}",
            'amounts': f"{self.amounts}",
            'amount tag': f"{self.amounts_tag}",
            'id': f'{self.id}',
        }

    @staticmethod
    def actual_date():
        return datetime.now()

    def update_status(self):
        self.statuses = self.get_next_status()
        self.jfs.update_file(self.name_file, UPLOAD_FILE)

    def downgrade_status_v2(self):
        self.statuses = self.get_downgrade_status()
        self.jfs.update_file(self.name_file, UPLOAD_FILE)

    def get_next_status(self):
        if self.current_status <= len(self.status) - 1:
            self.current_status += 1
        return self.status[self.current_status]

    def get_downgrade_status(self):
        if self.current_status > 0:
            self.current_status -= 1
        return self.status[self.current_status]

    def check_status(self):
        if all(obj[STATUS] == DONE for obj in self.subitems):
            self.update_status()
        if any(obj[STATUS] == INPROGRESS for obj in self.subitems):
            self.update_status()

    def add_sub_item(self, id_subitem):
        self.sub_item.append(id_subitem)

    def move_status(self):
        if self.statuses == INPROGRESS and any(
                [subitem[STATUS].__eq__(DONE) for subitem in
                 self.subitems]):
            for subitem in self.subitems:
                if subitem[ID] in self.sub_item:
                    subitem[STATUS] = DONE
            self.update_status()

    def downgrade_status(self):
        if self.statuses != TODO:
            self.downgrade_status_v2()
            for subitem in self.subitems:
                if subitem[ID] in self.sub_item and subitem[STATUS] != TODO:
                    subitem[STATUS] = self.statuses

    def get_custom_status(self):
        v1 = View()
        result = v1.get_attribute(CUSTOM_STATUS)
        self.custom_status = result

    def close_item(self):
        self.status = DONE

    def amount_items(self):
        item = ItemService().read()
        cnt = Counter()
        for obj in item:
            if obj[ROADMAP].id == self.id:
                for key, value in obj.items():
                    if key == STATUS:
                        cnt[value] += 1
        self.amounts = cnt

    def amount_tag_items(self):
        item = ItemService().read()
        cnt = Counter()
        for obj in item:
            if obj[ROADMAP].id == self.id:
                for key, value in obj.items():
                    if key == TAG:
                        cnt[value] += 1
        self.amounts_tag = cnt
