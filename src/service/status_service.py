from src.model.status import Status


class StatusService:

    def __init__(self):
        self.status = None

    def create_status(self, name: str):
        self.status = Status(name)

    def read_status(self):
        return f'Name: {self.status.name}'

    def update_status(self, key: str, new_value: str):
        status = vars(self.status)
        status[key] = new_value

    def delete_status(self):
        del self.status


