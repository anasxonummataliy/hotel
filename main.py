from utils import *
from user import user
from admin import admin
from termcolor import colored


def main():
    """Asosiy dastur"""
    while True:
        clear_console()
        draw_box("MEHMONXONA BOSHQARUV TIZIMI", "green")

        print(colored("\n1. Mijoz", "yellow"))
        print(colored("2. Admin", "yellow"))
        print(colored("0. Chiqish", "cyan"))

        choice = input(colored("\nTanlov >>> ", "magenta"))

        match choice:
            case "1":
                user()
            case "2":
                admin()
            case "0":
                print(colored("\n✔ Dastur tugatildi. Xayr! 👋", "green"))
                break
            case _:
                print(colored("\n❌ Noto'g'ri tanlov! Qayta kiriting.", "red"))
                input(colored("Davom etish uchun Enter...", "cyan"))


if __name__ == "__main__":
    main()
