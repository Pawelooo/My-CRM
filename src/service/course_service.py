from src.model.author import Author
from src.model.category import Category
from src.model.course import Course


class CourseService:

    def __init__(self):
        self.course = None

    def create_course(self, name: str, category: Category, author: Author, link: str = None, topic: str = None,):
        self.course = Course(name, category, author, link, topic)

    def read_course(self):
        return f'Name: {self.course.name}, Category: {self.course.category}, Author: {self.course.author}, ' \
               f'Topic: {self.course.topic}'

    def update_course(self, key: str, new_value: str):
        course = vars(self.course)
        course[key] = new_value

    def delete_course(self):
        del self.course


