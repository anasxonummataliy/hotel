from utils import *

class Admin:
    def __init__(self):
        self._login = 'admin'
        self.__password = 'admin'

    def login(self):
        while True:
            while True:
                draw_box("ADMIN PANEL")
                login = input(colored("\nLogin >>> ", 'magenta'))
                password = input(colored("Parol >>> ", 'magenta'))
                if login == self._login:
                    if password == self.__password:
                        print(colored('\nXush kelibsiz!\n', 'green'))
                        return
                    else:
                        print(colored("\nParolni xato kiritdingiz.\nQayta kiriting❗️", 'red'))
                        break
                else:
                    print(colored("\nLoginni xato kiritdingiz.\nQayta kiriting❗️", "red"))
                    break

    def menu(self):
        while True:
            while True:
                clear_console()
                draw_box('ADMIN MENU')
                print(colored("1. Xonalar", 'yellow'))
                print(colored("2. Barcha bronlar", 'yellow'))
                print(colored("3. Hisobot", 'yellow'))
                print(colored("4. Mijozlar ro'yhati", 'yellow'))
                print(colored("0. Chiqish", "cyan"))
                
                choice = input(colored("Tanlov >>> ", 'magenta'))




    


obj_admin = Admin()

def admin():
    while True:
        obj_admin.login()
        obj_admin.menu()



admin()