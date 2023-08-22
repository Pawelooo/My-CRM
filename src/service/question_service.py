import random

from src.model.config import FILE_LOCATION, FILE_QUESTION

from src.model.question import Question
from src.model.respository import Repository



class QuestionService:

    def __init__(self):
        self.repository = Repository()
        self.used_questions = []

    def create(self, obj: Question):
        self.repository.create(f'{FILE_LOCATION}{FILE_QUESTION}', obj)

    def read(self):
        return self.repository.find_all(f'{FILE_LOCATION}{FILE_QUESTION}')

    def update(self, obj: Question, key: str):
        self.repository.update(f'{FILE_LOCATION}{FILE_QUESTION}', obj, key)

    def delete(self, key: str):
        self.repository.delete(f'{FILE_LOCATION}{FILE_QUESTION}', key)

    def get_random_with_parametrization(self, parametrization):
        questions_all = self.repository.find_all(
            f'{FILE_LOCATION}{FILE_QUESTION}')
        return random.choice([question for question in questions_all
                              if question['Tag'] == parametrization])

    def get_random_question(self):
        return random.choice(self.repository.find_all(f'{FILE_LOCATION}'
                                                      f'{FILE_QUESTION}'))

    def get_unique_question(self):
        questions = list({question['name']: question for question
                          in self.repository.find_all(
                f'{FILE_LOCATION}{FILE_QUESTION}')}.values())
        while True:
            rd_question = random.choice(questions)
            if rd_question not in self.used_questions:
                self.used_questions.append(rd_question)
                return rd_question

    def get_random_with_parametrization(self, parametrization):
        questions_all = self.repository.find_all(
            f'{FILE_LOCATION}{FILE_QUESTION}')
        return random.choice([question for question in questions_all if question['Tag'] == parametrization])
