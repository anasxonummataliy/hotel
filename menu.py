<<<<<<< HEAD
from utils import *
from user import *
from  auth import register


def menu():
    pass
=======
from datetime import datetime
from storage import *
from utils import *
from termcolor import colored
from pprint import pprint


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
                    show_profile()
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
    rooms = get_data('data/rooms.json')
    while True:
        show_available_rooms()
        while True:
            choice = input(colored("Qaysi xonani bron qilasiz? (raqam kiriting) >>> ", "magenta"))
            available_rooms = [room for room in rooms if room['status']== 'Bo\'sh']
            available_rooms_numbers = [num['number'] for num in available_rooms]
            if choice.isdigit() or int(choice) not in available_rooms_numbers:
                print(colored("Xato raqam kiritdingiz.\nQayta kiriting❗️", "red"))
                break
            return
    
bookings(1)


#         show_available_rooms()
#         try:
#             tanlov = int(input("Qaysi xonani bron qilasiz? (raqam kiriting): "))
#         except ValueError:
#             print("Raqam kiriting!")
#             return

#         available_rooms = [r for r in rooms if r["status"] == "Available"]
#         if tanlov < 1 or tanlov > len(available_rooms):
#             print("Noto'g'ri tanlov!")
#             return

#         tanlangan = available_rooms[tanlov - 1]

#         check_in = input("Check-in sanasini kiriting (YYYY-MM-DD): ")
#         check_out = input("Check-out sanasini kiriting (YYYY-MM-DD): ")

#         try:
#             date_in = datetime.strptime(check_in, "%Y-%m-%d")
#             date_out = datetime.strptime(check_out, "%Y-%m-%d")
#             if date_out <= date_in:
#                 print("Check-out sanasi check-in sanasidan oldin bo'lishi mumkin emas!")
#                 return
#         except:
#             print("Sanani YYYY-MM-DD formatida kiriting!")
#             return

#         total_days = (date_out - date_in).days
#         total_price = total_days * tanlangan["price"]

#         booking_id = 1
#         if bookings:
#             booking_id = max(b["id"] for b in bookings) + 1

#         new_booking = {
#             "id": booking_id,
#             "user_id": profil["id"],
#             "room_id": tanlangan["id"],
#             "check_in": check_in,
#             "check_out": check_out,
#             "total_price": total_price,
#             "status": "Pending",
#         }

#         bookings.append(new_booking)
#         write(bookings_file, bookings)

#         tanlangan["status"] = "Occupied"
#         write(rooms_file, rooms)

#         print(f"Xona {tanlangan['number']} muvaffaqiyatli bron qilindi!")
#         print(f"Umumiy narx: {total_price} so'm. Status: Pending")


# my_bookings da muammo bor
# profile orqali password o'zgartirish kerak
# bronlar yo'q bo'lsa bronlar yo'q deyishi kerak
>>>>>>> origin/main
