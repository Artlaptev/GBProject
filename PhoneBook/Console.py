
#import os 

class Console:
    def WriteLine(self, line:str):
        print(line)

    def ReadLine(self, line:str):
        return input(line)

    def Clear(self):
        #os.system('cls' if os.name == 'nt' else 'clear')
        #os.system('clear')
        print(' 1 ')