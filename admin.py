from utils import *

class Admin:
    def __init__(self):
        self._login = 'admin'
        self.__password = 'admin'

    def login(self):
        while True:
            while True:
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
                pass


    


obj_admin = Admin()

def admin():
    while True:
        draw_box("ADMIN PANEL")
        obj_admin.login()
        obj_admin.menu()



admin()
