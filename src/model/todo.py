from src.model.book import Book
from src.model.course import Course
from src.model.generator import Generator
from src.model.user import User
from src.model.video import Video


class ToDo:

    def __init__(self, user: User, video: Video = None, course: Course = None, book: Book = None):
        self.id = Generator().generate_number()
        self.user = user
        self.video = video
        self.course = course
        self.book = book

    def __repr__(self):
        return {
            'user': self.user,
            'video': self.video if self.video else '',
            'course': self.course if self.course else '',
            'book': self.book if self.book else ''
        }
