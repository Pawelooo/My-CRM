from ast import literal_eval

from src.model.config import CONTENT_ENCODE
from src.model.validator import Validator


class JfsValidator(Validator):

    def validate(self, result):
        result_status = result.status_code
        if 200 >= result_status < 400:
            return None
        result_content = literal_eval(result.content.decode(CONTENT_ENCODE))['messages']
        if 400 >= result_status < 500:
            return self.create_validation(result_content)
        if result_status >= 500:
            return self.create_validation(result_content)

    def create_validation(self, code):
        text = f'{code}'
        return text
