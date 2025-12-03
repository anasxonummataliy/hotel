from utils import *
from termcolor import colored
from auth import *
from admin import admin
from user import user


def start_project():
    draw_box("PDP Hotel")
    print()
    print(colored('1. Mijoz\n2. Admin\n3. Chiqish\n', 'yellow'))
    choice = input(colored("Tanlov >>> ", 'magenta'))
    match choice:
        case '1':
            user()
        case '2':
            admin()
        case '3':
            exit()


start_project()
