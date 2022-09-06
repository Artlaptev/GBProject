from View import UserInterface
import contact_book

class Controller:

    Book = contact_book.contact_book()
    ConPrint = UserInterface()

    def __init__(self, book, conPrint):
        self.Book = book
        self.ConPrint = conPrint    

    def Load_Data(self):
        self.ConPrint.Print_Menu_Load()
        res = self.ConPrint.Read_Line()
        if res == '1': 
            return
        if res == '2':
            return
        #вместо return будет реализация  

    def StartLoad(self):
        self.Book._contacts = []

    def Search(self, id_Command):
        result = None
        try:
            if id_Command == 1:
                id = int(self.ConPrint.Read_Line('Введите id: '))
                result = self.Book.get_by_id(id)
                self.ConPrint.Print_List_Book(result)
            else:
                surname = self.ConPrint.Read_Line('Введите фамилию: ')
                result = self.Book.get_by_surname(surname)
                for user in result:
                    self.ConPrint.Print_List_Book(user)        
        except:
            print('error')
            return

        if result == [] and result == None:
            print('не нашел')

    def Add_User(self):
        name =   self.ConPrint.Read_Line('Введите имя ')
        patronymic = self.ConPrint.Read_Line('Введите отчество ')
        surname = self.ConPrint.Read_Line('Введите фамилию ')
        number = self.ConPrint.Read_Line('Введите номер ')

        self.Book.add_contact(name, patronymic, surname, number)

    def Print_Book(self):
        res = self.Book.get_unsorted()
        for i in range(len(res)):
            self.ConPrint.Print_List_Book(res[i])
        self.ConPrint.Read_Line('')

    def Delite(self):
        id = self.ConPrint.Read_Line('Введите id для удоления ')
        try:
            self.Book.delete_contact(int(id))
        except:
            print('error')