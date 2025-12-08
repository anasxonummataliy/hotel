from termcolor import colored
from utils import *
from auth import *
from menu import menu


def user():
    while True:
        while True:
            draw_box("PDP Hotel")
            print(colored("\n1. Ro'yhatdan o'tish\n2. Kirish\n3. Orqaga \n", "yellow"))
            choice = input(colored("Tanlov >>> ", "magenta"))
            match choice:
                case "1":
                    user_id = register()
                    menu(user_id)
                case "2":
                    login()
                    menu()
                case "3":
                    return
                case _:
                    print(
                        colored(
                            "Siz xato ma'lumot kiritdingiz!\n Qayta kiriting.", "red"
                        )
                    )
                    input(colored("Davom etish uchun enterni bosing...", "green"))
                    clear_console()
                    break