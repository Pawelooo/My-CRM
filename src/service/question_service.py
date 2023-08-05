import random

from src.model.config import FILE_LOCATION, FILE_QUESTION

from src.model.respository import Repository



class QuestionService:

    def __init__(self):
        self.repository = Repository()

    def get_random_question(self):
        return random.choice(self.repository.find_all(f'{FILE_LOCATION}'
                                                      f'{FILE_QUESTION}'))
