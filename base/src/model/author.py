from base.src.model.generator import Generator


class Author:

    def __init__(self, name: str, surname: str, website: str = None, country: str = None, topic: str = None):
        self.id = Generator().generate_number()
        self.name = name
        self.surname = surname
        self.website = website
        self.country = country
        self.topic = topic

    def __repr__(self):
        return {
            "name": f"{self.name}",
            "surname": f"{self.surname}",
            "website": f"{self.website}" if self.website is not None else "",
            "country": f"{self.country}" if self.country is not None else "",
            "topic": f"{self.topic}" if self.topic is not None else "",
            "id": f"{self.id}"
        }
