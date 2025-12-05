from storage import *
from utils import *
from termcolor import colored
from pprint import pprint


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
                    show_room()
                    clear_console()
                case "2":
                    "bookings"
                    clear_console()
                case "3":
                    my_bookings(user_id)
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
    rooms = get_data("data/rooms.json")
    draw_box("Bo'sh xonalar")
    print()
    print(
        colored(
            f"{'Xona Raqami':<5} | {'Turi':<5} | {'Narxi':<11} | {'Holati':<10}",
            "cyan",
            attrs=["bold"],
        )
    )
    for room in rooms:
        if room["status"] == "Bo'sh":
            print(
                colored(
                    f"№: {room['number']:<8} | {room['type']:<5} | {room['price']:>5} so'm | {room['status']:<10}",
                    "yellow",
                )
            )


def my_bookings(user_id):
    draw_box("Mening bronlarim")
    print()
    bookings = get_data("data/bookings.json")
    print(
        colored(
            f"{'Bron ID':<8} | {'Xona ID':<8} | {'Kirish':<12} | {'Chiqish':<12} | {'Narxi':<15} | {'Holati':<12}",
            "cyan",
            attrs=["bold"],
        )
    )
    print(colored("═" * 95, "cyan"))
    for booking in bookings:
        if booking["user_id"] == user_id:
            print(
                colored(
                    f"{booking['id']:<8} | {booking['room_id']:<8} | {booking['check_in']:<12} | {booking['check_out']:<12} | {booking['total_price']:<10} so'm | {booking['status']:<12}",
                    "yellow",
                )
            )

def show_profile(user_id):
    users = get_data('data/users.json')
    for user in users:
        if user['id'] == user_id:
            pass

