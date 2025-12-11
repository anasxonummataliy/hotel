from utils import *
from user import user
from admin import Admin
from termcolor import colored



def main():
    while True:
        clear_console()
        draw_box("MEHMONXONA BOSHQARUV TIZIMI", "green")

        print(colored("\n1. Mijoz", "yellow"))
        print(colored("2. Admin", "yellow"))
        print(colored("0. Chiqish", "cyan"))

        choice = input(colored("\nTanlov >>> ", "magenta"))
        admin = Admin()

        match choice:
            case "1":
                user()
            case "2":
                admin.start()
            case "0":
                print(colored("\n✔ Dastur tugatildi. Xayr! 👋", "green"))
                exit()
            case _:
                print(colored("\n❌ Noto'g'ri tanlov! Qayta kiriting.", "red"))
                input(colored("Davom etish uchun Enter...", "cyan"))


if __name__ == "__main__":
    main()
