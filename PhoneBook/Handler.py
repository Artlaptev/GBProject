from contact import contact
from contact_book import contact_book
import json
import xml.etree.ElementTree as ET

from abc import ABC, abstractmethod


def create_contact_by_dictionary(book, item):
    book.add_contact(item['name'], item['patronymic'], item['surname'], item['number'])


class JsonHandler():
    def importin(self):
        file = open('test.json')
        data = json.load(file)
        book = contact_book()
        for item in data:
            create_contact_by_dictionary(book, item)
        return book

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


class XMLHandler():
    def importin(self):
        book = contact_book()
        tree = ET.parse('test.xml')
        root = tree.getroot()
        for contact_xml in root:
            dict_atrs = {}
            for atr in contact_xml:
                dict_atrs[atr.tag] = atr.text
            print(dict_atrs)
            create_contact_by_dictionary(book, dict_atrs)
        return book

    def export(self, lst):
        data = ET.Element('CONTACTLIST')
        for item in lst:
            contact = ET.SubElement(data, 'CONTACT')
            self.create_subel(contact, 'id', item.id)
            self.create_subel(contact, 'name', item.name)
            self.create_subel(contact, 'patronymic', item.patronymic)
            self.create_subel(contact, 'surname', item.surname)
            self.create_subel(contact, 'number', item.number)
        dataxml = ET.tostring(data).decode('utf-8')
        file = open('test.xml', 'w')
        file.write(dataxml)

    def create_subel(self, element, name, value):
        subEL = ET.SubElement(element, name)
        subEL.text = str(value)


handler=JsonHandler()
book=handler.importin()
handler1 = XMLHandler()
handler1.export(book.get_sorted())
handler1.importin()
