import random

from src.model.config import FILE_LOCATION, FILE_QUESTION, FILE_TAG
from src.model.question import Question
from src.model.respository import Repository
from src.service.tags.tag import Tag


class QuestionService:

    def __init__(self):
        self.repository = Repository()

    def get_random_with_parametrization(self, parametrization):
        questions_all = self.repository.find_all(
            f'{FILE_LOCATION}{FILE_QUESTION}')
        return random.choice([question for question in questions_all
                              if question['Tag'] == parametrization])

