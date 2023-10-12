from ast import literal_eval

from src.model.config import FILE_ENCODING
from src.model.validator_status_code import ValidatorStatus


class JfsValidator(ValidatorStatus):

    def validate(self, result):
        result_status = result.status_code
        if 200 >= result_status < 400:
            return None
        result_content = literal_eval(result.content.decode(FILE_ENCODING))['messages']
        if 400 >= result_status < 500:
            return self.create_validation(result_content)
        if result_status >= 500:
            return self.create_validation(result_content)

    def create_validation(self, code):
        text = f'{code}'
        return text
