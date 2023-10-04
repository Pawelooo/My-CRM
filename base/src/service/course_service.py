from base.src.model.config import FILE_LOCATION, FILE_COURSE_NAME, FILE_AUTHOR_NAME
from base.src.model.course import Course
from base.src.model.respository import Repository


class CourseService:

    def __init__(self):
        self.repository = Repository()

    def create(self, obj: Course):
        self.repository.create(f'{FILE_LOCATION}{FILE_COURSE_NAME}', obj)

    def read(self):
        return self.repository.find_all(f'{FILE_LOCATION}{FILE_AUTHOR_NAME}')

    def update(self, obj: Course, key: str):
        self.repository.update(f'{FILE_LOCATION}{FILE_COURSE_NAME}', obj, key)

    def delete(self, key: str):
        self.repository.delete(f'{FILE_LOCATION}{FILE_COURSE_NAME}', key)


