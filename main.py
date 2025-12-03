from utils import *
from termcolor import colored
from auth import *


def start_project():
    draw_box("PDP Hotel")
    print()
    print(colored('1. Mijoz\n2. Admin\n3. Chiqish\n', 'yellow'))
    choice = input(colored("Tanlov >>> ", 'magenta'))
    match choice:
        case '1':
            register()
        case '2':
            print('admin')
        case '3':
            exit()

if __name__ == '__main__':
    start_project()
