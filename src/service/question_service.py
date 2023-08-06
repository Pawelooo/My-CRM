
import random
from src.model.config import FILE_LOCATION, FILE_QUESTION, FILE_TAG
from src.model.question import Question
from src.model.respository import Repository
from src.service.tags.tag import Tag


class QuestionService:

    def __init__(self):
        self.repository = Repository()

    def create(self, obj: Question):
        self.repository.create(f'{FILE_LOCATION}{FILE_QUESTION}', obj)

    def read(self):
        return self.repository.find_all(f'{FILE_LOCATION}{FILE_QUESTION}')

    def update(self, obj: Question, key: str):
        self.repository.update(f'{FILE_LOCATION}{FILE_QUESTION}', obj, key)

    def delete(self, key: str):
        self.repository.delete(f'{FILE_LOCATION}{FILE_QUESTION}', key)
        
    def get_random_question(self):
        return random.choice(self.repository.find_all(f'{FILE_LOCATION}'
                                                      f'{FILE_QUESTION}'))


