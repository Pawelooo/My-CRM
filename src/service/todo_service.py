from src.model.author import Author
from src.model.book import Book
from src.model.category import Category
from src.model.course import Course
from src.model.todo import ToDo
from src.model.user import User
from src.model.video import Video


class ToDoService:

    def __init__(self):
        self.todo = None

    def create_todo(self, user: User, video: Video, course: Course, book: Book):
        self.todo = ToDo(user, video, course, book)

    def read_todo(self):
        return f'User: {self.todo.name}, Video: {self.todo.video}, Course: {self.todo.course},' \
               f'Book: {self.todo.book}'

    def update_todo(self, key: str, new_value: str):
        todo = vars(self.todo)
        todo[key] = new_value

    def delete_todo(self):
        del self.todo


