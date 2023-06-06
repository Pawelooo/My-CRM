"""
Once data with present should be found
"""
class Generator:

    def __init__(self):
        self.current_id = 0

    def generate_number(self):
        self.current_id += 1
        return self.current_id

