#from curses import intrflush

#from curses.ascii import US


class UserInterface:
    def PrintMenu():
        con = Console()

        #con.Clear()
        con.WriteLine('\n\t\tТелефонная книга')
        con.WriteLine('======================================================')
        con.WriteLine('\n\tКоманды:\n\t    1 - добавить\n\t    2 - вывести на экран список\n\t    3 - удолить\n\t    0 - выход')

    def ReadLine():
        con = Console()
        return con.ReadLine('\n\tВведите гомер команды:')
    
    def PrintListBook(self, lisrUsers):
        for line in lisrUsers():
            self.ReadLine(line)

class Console:
    def WriteLine(self, line:str):
        print(line)

    def ReadLine(self, line:str):
        return input(line)

    #def Clear(self):
        #print('222222')
        #print(50*'\n')