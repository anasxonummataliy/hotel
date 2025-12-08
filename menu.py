from datetime import datetime
from storage import *
from utils import *
from termcolor import colored
from pprint import pprint

file_name = "data/users.json"

def menu(user_id):
    while True:
        while True:
            clear_console()
            draw_box("Mehmonxona Menu")
            print(colored("\n1. Bo'sh xonalar", "yellow"))
            print(colored("2. Bron qilish", "yellow"))
            print(colored("3. Mening bronlarim", "yellow"))
            print(colored("4. Profil", "yellow"))
            print(colored("0. Chiqish", "cyan"))

            choice = input(colored("\nTanlov >>> ", "magenta"))
            match choice:
                case "1":
                    clear_console()
                    show_available_rooms()
                    input(colored("\nDavom etish...", "green"))
                case "2":
                    clear_console()
                    bookings(user_id)
                    input(colored("\nDavom etish...", "green"))
                case "3":
                    clear_console()
                    my_bookings(user_id)
                    input(colored("\nDavom etish...", "green"))
                case "4":
                    clear_console()
                    show_profile(user_id)
                    input(colored("\nDavom etish...", "green"))
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


def show_available_rooms():
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

    user_has_booking = False  # <<< qo'shildi

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
            user_has_booking = True
            print(
                colored(
                    f"{booking['id']:<8} | {booking['room_id']:<8} | {booking['check_in']:<12} | {booking['check_out']:<12} | {booking['total_price']:<10} so'm | {booking['status']:<12}",
                    "yellow",
                )
            )

    if not user_has_booking:
        print(colored("Sizda hozircha bronlar mavjud emas!", "red"))


def show_profile(user_id):
    users = get_data("data/users.json")
    draw_box("Profil")
    print()
    for user in users:
        if user["id"] == user_id:
            print(colored("Ism : ", "yellow"), end="")
            print(colored(f"{user['first_name']}", "magenta"))
            print(colored("Familiya : ", "yellow"), end="")
            print(colored(f"{user['last_name']}", "magenta"))
            print(colored("Telefon : ", "yellow"), end="")
            print(colored(f"{user['phone']}", "magenta"))
            break


def bookings(user_id):
    show_available_rooms()
    pass

def change_passsword():
    pass

# my_bookings da muammo tuzatildi
# bronlar bo‘lmasa – to‘g‘ri xabar chiqaradi
