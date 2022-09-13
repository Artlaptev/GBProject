from contact import contact
from contact_book import contact_book
import json
import xml.etree.ElementTree as ET
import os.path

from abc import ABC, abstractmethod


def create_contact_by_dictionary(item):
    cont = contact(int(item['id']), item['name'], item['patronymic'], item['surname'], item['number'])
    return cont


class JsonHandler():
    def importin(self):
        book = []
        file_paths = 'data\\database.json'
        if not os.path.exists(file_paths):
            return []
        file = open(file_paths)
        data = json.load(file)
        for item in data:
            book.append(create_contact_by_dictionary(item))
        return book

    def export(self, contact_list):
        data = []
        for item in contact_list:
            data.append(JsonHandler.get_dict(item))
        file = open('data\\database.json', 'w')
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
        book = []
        file_paths = 'data\\database.xml'
        if not os.path.exists(file_paths):
            return book
        tree = ET.parse(file_paths)
        root = tree.getroot()
        for contact_xml in root:
            dict_atrs = {}
            for atr in contact_xml:
                dict_atrs[atr.tag] = atr.text
            print(dict_atrs)
            book.append(create_contact_by_dictionary(dict_atrs))
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
        file = open('data\\database.xml', 'w')
        file.write(dataxml)

    def create_subel(self, element, name, value):
        subEL = ET.SubElement(element, name)
        subEL.text = str(value)

# handler=JsonHandler()
# book=handler.importin()
# handler1 = XMLHandler()
# handler1.export(book.get_sorted())
# handler1.importin()


# book=[]
# con1=contact(1,'artem','ram','lap','323125432')
# con2=contact(2,'ivan','petrovicc','ggg','3231sdfs5432')
# book.append(con1)
# book.append(con2)
# xml=XMLHandler()
# xml.export(book)
# JsonHandler.export(book)
# handler=JsonHandler()
# imported_book=handler.importin()
# print(imported_book)
