from src.model.config import FILE_LOCATION, FILE_COURSE_NAME
from src.model.course import Course
from src.model.respository import Repository


class CourseService:

    def __init__(self):
        self.repository = Repository()

    def create(self, obj: Course):
        self.repository.create(f'{FILE_LOCATION}{FILE_COURSE_NAME}', obj)

    def read(self, file_path: str):
        return self.repository.find_all(file_path)

    def update(self, obj: Course, key: str):
        self.repository.update(f'{FILE_LOCATION}{FILE_COURSE_NAME}', obj, key)

    def delete(self, key: str):
        self.repository.delete(f'{FILE_LOCATION}{FILE_COURSE_NAME}', key)


