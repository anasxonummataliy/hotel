from storage import *
from utils import *

class Admin:
    def __init__(self):
        self._login = 'admin'
        self.__password = 'admin'

    def login(self):
        while True:
            while True:
                draw_box("ADMIN PANEL")
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

    def get_all_rooms(self):
        rooms = get_data("data/rooms.json")
        draw_box("Xonalar")
        print()
        print(
            colored(
                f"{'Xona Raqami':<5} | {'Turi':<5} | {'Narxi':<11} | {'Holati':<10}",
                "cyan",
                attrs=["bold"],
            )
        )
        for room in rooms:
            print(
                    colored(
                        f"№: {room['number']:<8} | {room['type']:<5} | {room['price']:>5} so'm | {room['status']:<10}",
                        "yellow",
                    )
                )

    def menu(self):
        while True:
            while True:
                clear_console()
                draw_box('ADMIN MENU')
                print(colored("1. Xonalar", 'yellow'))
                print(colored("2. Barcha bronlar", 'yellow'))
                print(colored("3. Hisobot", 'yellow'))
                print(colored("4. Mijozlar ro'yhati", 'yellow'))
                print(colored("0. Chiqish", "cyan"))

                choice = input(colored("Tanlov >>> ", 'magenta'))
                match choice:
                    case "1":
                        self.get_all_rooms() 
                        input(colored("\nDavom etish uchun Enter bosing...", "cyan"))
                    case "2":
                        self.get_all_bookings()
                        input(colored("\nDavom etish uchun Enter bosing...", "cyan"))
                    case "3":
                        self.show_report()
                        input(colored("\nDavom etish uchun Enter bosing...", "cyan"))
                    case "4":
                        self.get_all_customers()
                        input(colored("\nDavom etish uchun Enter bosing...", "cyan"))
                    case "0":
                        print(colored("Xayr! 👋", "green"))
                        break
                    case _:
                        print(colored("Noto'g'ri tanlov!", "red"))
                        input(colored("\nDavom etish uchun Enter bosing...", "cyan"))


obj_admin = Admin()
def admin():
    while True:
        obj_admin.login()
        obj_admin.menu()


obj_admin.get_all_rooms()
