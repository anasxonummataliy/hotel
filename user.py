from termcolor import colored
import menu1
from utils import *
from auth import *
from menu1 import *


def user():
    while True:
        while True:
            draw_box("PDP Hotel")
            print(colored("\n1. Ro'yhatdan o'tish\n2. Kirish\n3. Orqaga \n", "yellow"))
            choice = input(colored("Tanlov >>> ", "magenta"))
            match choice:
                case "1":
                    register()
                    menu1()
                case "2":
                    login()
                    menu1()
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
