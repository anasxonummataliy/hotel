from termcolor import colored
from utils import *
from auth import *


def user():
    while True:
        while True:
            draw_box("PDP Hotel")
            print(colored('1. Ro\'yhatdan o\'tish\n2. Kirish\n3. Orqaga ', 'yellow'))
            choice = input(colored('Tanlov >>> ', 'magenta'))
            match choice:
                case '1':
                    flag = register()
                    if flag:
                        print('menu()')
                case '2':
                    flag = login()
                    if flag:
                        print('menu()')
                case '3':
                    return
                case _:
                    print(colored('Siz xato ma\'lumot kiritdingiz!\n Qayta kiriting.', 'red'))
                    input(colored('Davom etish uchun enterni bosing...', 'green'))
                    clear_console()
                    break
user()