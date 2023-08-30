from src.service.status_service import StatusService


class SubItem:

    def __init__(self):
        self.status_opt = StatusService()
        self.level = 0
        self.status = None
        self.update_status()

    def __repr__(self):
        return {
            'status': self.status
        }

    def update_status(self):
        obj = list(self.status_opt.read()[0].values())
        self.status = obj[self.level]
        if not self.level >= len(obj) - 1:
            self.level += 1
