from src.model.book import Book
from src.course.course import Course
from src.model.user import User
from src.model.video import Video


class ToDo:

    def __init__(self, user: User, video: Video, course: Course, book: Book):
        self.user = user
        self.video = video
        self.course = course
        self.book = book
