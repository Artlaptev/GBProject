
from ast import parse
from View import UserInterface
import contact_book 


class Program:
    Book = contact_book.contact_book()
    ConPrint = UserInterface()

    def Run(self):
        Do = True
        #ConPrint = View.UserInterface()

        while Do:
            #self.ConPrint.PrintMenu()
            UserInterface.PrintMenu()
            Do = self.Do_Commands(UserInterface.ReadLine())

    def Do_Commands(self, id_command):
        if id_command == '0':
            return False
        elif id_command == '1':
            self.Add_User()
        elif id_command == '2':
            self.Print_Book()
        elif id_command == '3':
            self.Delite()

        return True

    def Add_User(self):
        name =  UserInterface.ReadLine('Введите имя ')
        patronymic = UserInterface.ReadLine('Введите отчество ')
        surname = UserInterface.ReadLine('Введите фамилию ')
        number = UserInterface.ReadLine('Введите номер ')

        self.Book.add_contact(name, patronymic, surname, number)

    def Print_Book(self):
        res = self.Book.get_unsorted()
        for i in range(len(res)):
            self.ConPrint.PrintListBook(res[i])

    def Delite(self):
        id = UserInterface.ReadLine('Введите id для удоления ')
        try:
            self.Book.delete_contact(int(id))
        except:
            print('error')


pro =  Program()
pro.Run()