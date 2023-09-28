from src.model.config import FILE_SUBITEM, FILE_STATUS_NAME, UPLOAD_FILE, \
    GET_FILE, CUSTOM_STATUS, TAG

from src.model.config import DONE

from collections import Counter
from src.model.config import STATUS, ROADMAP, UPLOAD

from collections import Counter


from src.model.generator import Generator
from src.service.jfs import JsonFromService
from src.service.subitem_service import SubItemService
from src.service.tags.tag import Tag
from src.view.view import View


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
        self.name_file = name_file
        self.attachments = JsonFromService().add_file(self.name_file,
                                                      UPLOAD_FILE)
        self.status_opt = JsonFromService().read_file(FILE_STATUS_NAME,
                                                      GET_FILE)
        self.status = None
        self.comments = None
        self.roadmap = None
        self.tag = tag
        self.current_status = 0
        self.jfs = JsonFromService()
        self.custom_status = None
        self.amounts = None
        self.amount_tag = None

    def __repr__(self):
        return str({
            "id": f"{self.id}",
            "name": f"{self.name}",
            "title": f"{self.title}",
            "description": f"{self.description}",
            "id_item": f"{self.id_item}",
            "opened by": f"{self.opened_by}",
            "deadline": f"{self.deadline}",
            "status": f"{self.status}",
            "name_file": f"{self.name_file}",
            "attachments": f"{self.attachments}",
            "tag": f"{self.tag}",
            'amounts': f"{self.amounts}",
            'amounts tag': f"{self.amounts}"
        })

    def update_status(self):
        self.status = self.get_next_status()
        self.jfs.update_file(self.name_file, UPLOAD_FILE)

    def get_next_status(self):
        if self.current_status <= len(self.status) - 1:
            self.current_status += 1
        return self.status[self.current_status]

    def get_custom_status(self):
        v1 = View()
        result = v1.get_attribute(CUSTOM_STATUS)
        self.custom_status = result

    def close_item(self):
        self.status = DONE

    def amount_subitems(self):
        subitem = SubItemService().read()
        cnt = Counter()
        for obj in subitem:
            if obj[ROADMAP].id == self.id:
                for key, value in obj.items():
                    if key == STATUS:
                        cnt[value] += 1
        self.amounts = cnt

    def amount_tag_subitems(self):
        subitem = SubItemService().read()
        cnt = Counter()
        for obj in subitem:
            if obj[ROADMAP].id == self.id:
                for key, value in obj.items():
                    if key == TAG:
                        cnt[value] += 1
        self.amounts_tag = cnt

