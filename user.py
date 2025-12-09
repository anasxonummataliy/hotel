from termcolor import colored
from utils import *
from auth import *
from menu import menu


def user():
    while True:
        clear_console()
        draw_box("PDP Hotel")
        print(colored("\n1. Ro'yhatdan o'tish", "yellow"))
        print(colored("2. Kirish", "yellow"))
        print(colored("0. Orqaga", "cyan"))

        choice = input(colored("\nTanlov >>> ", "magenta"))

        match choice:
            case "1":
                user_id = register()
                if user_id:
                    menu(user_id)
            case "2":
                user_id = login()
                if user_id:
                    menu(user_id)
                else:
                    print(colored("\n❌ Tizimga kirib bo'lmadi!", "red"))
                    input(colored("Davom etish uchun Enter...", "cyan"))
            case "0":
                return
            case _:
                print(colored("\n❌ Noto'g'ri tanlov! Qayta kiriting.", "red"))
                input(colored("Davom etish uchun Enter...", "cyan"))
