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
                                                      "upload/")
        self.status = None
        self.comments = None
        self.roadmap = None
        self.tag = tag

    def __repr__(self):
        return str({
            "id": f"{self.id}",
            "name": f"{self.name}",
            "title": f"{self.title}",
            "description": f"{self.description}",
            "id_item": f"{self.id_item}",
            "opened by": f"{self.opened_by}",
            "deadline": f"{self.deadline}",
            "done": f"{self.done}",
            "status": f"{self.status}",
            "name_file": f"{self.name_file}",
            "attachments": f"{self.attachments}",
            "tag": f"{self.tag}",
        })
