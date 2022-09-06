
from os import lseek
from Console import Console


class UserInterface:
    con = Console()

    def Print_Menu(self):

        #con.Clear()
        self.con.WriteLine('\n\t\tТелефонная книга')
        self.con.WriteLine('======================================================')
        self.con.WriteLine('\n\tКоманды:\n\t    1 - добавить\n\t    2 - вывести на экран список\
        \n\t    3 - удолить\n\t    4 - поиск по id\n\t    5 - поиск по фамилии\n\t    6 - загрузить\n\t    0 - выход')
    
    def Print_Menu_Load(self):
        self.con.WriteLine('\n\t\tТелефонная книга')
        self.con.WriteLine('======================================================')
        self.con.WriteLine('\n\t 1 - загрузить с помощью json    \n\t 2 - загрузить с помощью html')

    def Read_Line(self, line = '\n\tВведите номер команды: '):
        con = Console()
        return con.ReadLine(line)
    
    def Print_List_Book(self, lisrUsers):
        self.con.WriteLine('id: {} name: {} patronymic: {} surname: {} number: {}'.format(
            lisrUsers.id, lisrUsers.name, lisrUsers.patronymic, lisrUsers.surname, lisrUsers.number))
        
    def Print_In_Display(self, line:str):
        self.con.WriteLine(line)
