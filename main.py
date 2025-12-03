from utils import *
from termcolor import colored
from auth import *
from admin import admin
from user import user


def start_project():
    while True:
        while True:
            draw_box("PDP Hotel")
            print()
            print(colored("1. Mijoz\n2. Admin\n3. Chiqish\n", "yellow"))
            choice = input(colored("Tanlov >>> ", "magenta"))
            match choice:
                case "1":
                    clear_console()
                    user()
                case "2":
                    clear_console()
                    admin()
                case "3":
                    exit()
                case _:
                    clear_console()
                    print(colored("Xato ma'lumot kiritdingiz❗️ \nQayta kiriting.", "red"))
                    input(colored("Davom etish uchun ENTERni bosing...", "green"))
                    clear_console()
                    break


start_project()