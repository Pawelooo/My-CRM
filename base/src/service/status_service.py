from base.src.model.config import FILE_LOCATION, FILE_STATUS_NAME
from base.src.model.respository import Repository
from base.src.model.status import Status


class StatusService:

    def __init__(self):
        self.repository = Repository()

    def create(self, obj: Status):
        self.repository.create(f'{FILE_LOCATION}{FILE_STATUS_NAME}', obj)

    def read(self, ):
        return self.repository.find_all(f'{FILE_LOCATION}{FILE_STATUS_NAME}')

    def update(self, obj: Status, key: str):
        self.repository.update(f'{FILE_LOCATION}{FILE_STATUS_NAME}', obj, key)

    def delete(self, key: str):
        self.repository.delete(f'{FILE_LOCATION}{FILE_STATUS_NAME}', key)


