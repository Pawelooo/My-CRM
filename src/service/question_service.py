import random

from src.model.config import FILE_LOCATION, FILE_QUESTION

from src.model.respository import Repository


class QuestionService:

    def __init__(self):
        self.repository = Repository()
        self.used_questions = []

    def get_unique_question(self):
        questions = self.repository.find_all(f'{FILE_LOCATION}{FILE_QUESTION}')
        question_not_used = [question for question in questions if
                             question not in
                             self.used_questions]
        while question_not_used:
            rd_question = random.choice(question_not_used)
            if rd_question not in self.used_questions:
                self.used_questions.append(rd_question)
                return rd_question
