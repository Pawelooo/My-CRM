class View:

    def print_message(self, msg: str) -> None:
        return print(msg)

    def get_attribute(self, msg: str):
        self.print_message(msg)
        return input()


