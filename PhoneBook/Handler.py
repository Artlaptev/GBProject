from contact import contact
from contact_book import contact_book
import json

from abc import ABC, abstractmethod


class Handler(ABC):
    def importin(self):
        pass

    def export(self):
        pass


class JsonHandler(Handler):
    def importin(self):
        file = open('test.json')
        data = json.load(file)
        for item in data:
            contact_book.add_contact(
                self, item.name, item.patronymic, item.surname, item.number
            )


    def export(contact_list):
        data = []
        for item in contact_list:
            data.append(JsonHandler.get_dict(item))
        file = open('test.json', 'w')
        json.dump(data, file)
        file.close()

    def get_dict(item):
        item = item
        dict = {'id': item.id,
                'name': item.name,
                'patronymic': item.patronymic,
                'surname': item.surname,
                'number': item.number
                }
        return dict


class XMLHandler(Handler):
    def importin(self):
        pass

    def export(self):
        pass
