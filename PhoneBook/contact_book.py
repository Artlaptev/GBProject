from contact import contact

class contact_book:
    _next_id : int = 0
    _contacts = []

    def add_contact(self, name       : str, 
                          patronymic : str, 
                          surname    : str, 
                          number     : str):
        self._contacts.append(contact(self._next_id, name, patronymic, surname, number))
        self._next_id += 1
    
    def get_by_id(self, id : int):
        for item in self._contacts:
            if item.id == id:
                return item

    def get_by_surname(self, surname : str):
        result = []
        for item in self._contacts:
            if item.surname == surname:
                result.append(item)
        return result

    def edit_contact(self, id         : int, 
                           name       : str = None, 
                           patronymic : str = None, 
                           surname    : str = None, 
                           number     : str = None):
        item = self.get_by_id(id)
        item.edit(name, patronymic, surname, number)

    def delete_contact(self, id : int):
        for item in self._contacts:
            if item.id == id:
                self._contacts.remove(item)
    
    def get_sorted(self):
        return sorted([item for item in self._contacts], key = lambda row: (row.surname,
                                                                            row.name,
                                                                            row.patronymic))

    def get_unsorted(self):
        return self._contacts