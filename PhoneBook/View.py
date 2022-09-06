
from os import lseek


class UserInterface:

    def PrintMenu():
        con = Console()

        #con.Clear()
        con.WriteLine('\n\t\tТелефонная книга')
        con.WriteLine('======================================================')
        con.WriteLine('\n\tКоманды:\n\t    1 - добавить\n\t    2 - вывести на экран список\n\t    3 - удолить\n\t    0 - выход')

    def ReadLine(line = '\n\tВведите номер команды:'):
        con = Console()
        return con.ReadLine(line)
    
    def PrintListBook(self, lisrUsers):
        con = Console()
        con.WriteLine('id {} name {} patronymic {} surname {} number {}'.format(
            lisrUsers.id, lisrUsers.name, lisrUsers.patronymic, lisrUsers.surname, lisrUsers.number))
        #print(res[i].id)

    def Print_In_Display(line:str):
        con = Console()
        con.WriteLine(line)

class Console:
    def WriteLine(self, line:str):
        print(line)

    def ReadLine(self, line:str):
        return input(line)

    #def Clear(self):
        #print('222222')
        #print(50*'\n')