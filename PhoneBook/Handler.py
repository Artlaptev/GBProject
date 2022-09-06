from contact import  contact
import contact_book
import json


from abc import ABC, abstractmethod

class Handler(ABC):
    def importin(self):
        pass
    def export(self):
        pass

class JsonHandler(Handler):
    def importin(self):
        pass
    def export(self, item):
        book=contact(item)
        print(type(book))


class XMLHandler(Handler):
    def importin(self):
        pass

    def export(self):
        pass