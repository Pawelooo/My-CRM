class tag:
    # fetch the data from database

    def __init__(self, name, init_values):
        self.name = name
        self.values = init_values  # the db should be updated accordingly

    def find_all(self):
        return self.values

    def get(self, value):
        it = iter(self.values)
        while True:
            try:
                element = next(it)
                if element.lower() == value.lower():
                    return element
            except StopIteration:
                break
        self.values.add(value)  # the db should be updated accordingly
        return self.get(value)
