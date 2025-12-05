from storage import *
from utils import *
from termcolor import colored


def menu(user_id):
    while True:
        while True:
            draw_box("Mehmonxona Menu")
            print(colored("1. Barcha xonalar", "yellow"))
            print(colored("2. Bron qilish", "yellow"))
            print(colored("3. Mening bronlarim", "yellow"))
            print(colored("4. Profil", "yellow"))
            print(colored("0. Chiqish", "clyan"))

            choice = input(colored("Tanlov >>> ", "magenta"))
            match choice:
                case "1":
                    # show_room()
                    clear_console()
                case "2":
                    "bookings"
                    clear_console()
                case "3":
                    # my_bookings
                    clear_console()
                case "4":
                    # show profil
                    clear_console()
                case "0":
                    print(
                        colored(
                            "Bizning xizmatimizdan foydalanganingiz uchun raxmat!",
                            "green",
                        )
                    )
                    exit()
                case _:
                    print(
                        "Noto'g'ri ma'lumot kiritdingiz.\nIltimos qayta kiriting!",
                        "red",
                    )


def show_room():
    rooms = get_data('data/rooms.json', 'r')


    for i, room in enumerate(rooms, 1):
        print(
            f"{i}. Xona {room['number']} | {room['type']} | {room['price']} so'm | {room['status']}"
        )

show_room()