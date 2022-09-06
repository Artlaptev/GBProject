
#from string import printable
#from this import s
import View


class Program:
    def Run(self):
        Do = True
        #ConPrint = View.UserInterface()

        while Do:
            View.UserInterface.PrintMenu()
            Do = self.Do_Commands(View.UserInterface.ReadLine())

    def Do_Commands(self, id_command):
        if id_command == '0':
            return False
        #elif id_command == 1:
            #вызов метода 
        #elif id_command == 2:
            #вызов метода 
        #elif id_command == 3:
            #вызов метода
        return True

pro =  Program()
pro.Run()