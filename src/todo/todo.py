from src.book.book import Book
from src.course.course import Course
from src.user.user import User
from src.video.video import Video


class ToDo:

    def __init__(self, user: User, video: Video, course: Course, book: Book):
        self.user = user
        self.video = video
        self.course = course
        self.book = book
