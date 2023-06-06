from src.model.book import Book
from src.model.course import Course
from src.model.generator import Generator
from src.model.user import User
from src.model.video import Video


class ToDo:

    def __init__(self, user: User, video: Video, course: Course, book: Book):
        self.id = Generator().generate_number()
        self.user = user
        self.video = video
        self.course = course
        self.book = book
