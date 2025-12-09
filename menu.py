from datetime import datetime, timedelta
from storage import *
from utils import *
from termcolor import colored


def menu(user_id):
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
                input(colored("\nDavom etish uchun Enter...", "green"))
            case "2":
                clear_console()
                create_booking(user_id)
                input(colored("\nDavom etish uchun Enter...", "green"))
            case "3":
                clear_console()
                my_bookings(user_id)
                input(colored("\nDavom etish uchun Enter...", "green"))
            case "4":
                clear_console()
                show_profile(user_id)
                input(colored("\nDavom etish uchun Enter...", "green"))
            case "0":
                print(
                    colored(
                        "\n✔ Bizning xizmatimizdan foydalanganingiz uchun raxmat!",
                        "green",
                    )
                )
                return
            case _:
                print(colored("\n❌ Noto'g'ri tanlov! Qayta kiriting.", "red"))
                input(colored("Davom etish uchun Enter...", "cyan"))


def show_available_rooms():
    rooms = get_data("data/rooms.json")
    draw_box("Bo'sh xonalar")
    print()
    print(
        colored(
            f"{'Raqam':<8} | {'Turi':<15} | {'Narxi':<15} | {'Holati':<10}",
            "cyan",
            attrs=["bold"],
        )
    )
    print(colored("─" * 60, "cyan"))

    available = False
    for room in rooms:
        if room["status"] == "Bo'sh":
            available = True
            print(
                colored(
                    f"№ {room['number']:<6} | {room['type']:<15} | {room['price']:>10} so'm | {room['status']:<10}",
                    "yellow",
                )
            )

    if not available:
        print(colored("Hozirda bo'sh xonalar yo'q.", "red"))


def create_booking(user_id):
    rooms = get_data("data/rooms.json")
    bookings_list = get_data("data/bookings.json")

    show_available_rooms()

    available_rooms = [room for room in rooms if room["status"] == "Bo'sh"]

    if not available_rooms:
        print(colored("\n❌ Hozirda bo'sh xonalar yo'q!", "red"))
        return

    available_room_numbers = [room["number"] for room in available_rooms]

    while True:
        room_choice = input(colored("\nXona raqamini kiriting >>> ", "magenta"))
        if not room_choice.isdigit():
            print(colored("❌ Faqat raqam kiriting!", "red"))
            continue

        room_number = int(room_choice)
        if room_number not in available_room_numbers:
            print(colored("❌ Bunday xona mavjud emas yoki band!", "red"))
            continue

        break

    selected_room = next(
        room for room in available_rooms if room["number"] == room_number
    )

    while True:
        check_in = input(colored("Kelish sanasi (YYYY-MM-DD) >>> ", "magenta"))
        try:
            check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
            if check_in_date < datetime.now():
                print(colored("❌ O'tgan sanani kirita olmaysiz!", "red"))
                continue
            break
        except ValueError:
            print(colored("❌ Noto'g'ri format! (Masalan: 2024-12-25)", "red"))

    while True:
        check_out = input(colored("Ketish sanasi (YYYY-MM-DD) >>> ", "magenta"))
        try:
            check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
            if check_out_date <= check_in_date:
                print(
                    colored(
                        "❌ Ketish sanasi kelish sanasidan katta bo'lishi kerak!", "red"
                    )
                )
                continue
            break
        except ValueError:
            print(colored("❌ Noto'g'ri format! (Masalan: 2024-12-26)", "red"))

    days = (check_out_date - check_in_date).days
    total_price = days * selected_room["price"]

    print(colored("\n" + "═" * 50, "cyan"))
    print(
        colored(
            f"Xona: № {selected_room['number']} - {selected_room['type']}", "yellow"
        )
    )
    print(colored(f"Kelish: {check_in}", "yellow"))
    print(colored(f"Ketish: {check_out}", "yellow"))
    print(colored(f"Kunlar soni: {days} kun", "yellow"))
    print(colored(f"Umumiy narx: {total_price:,} so'm", "green", attrs=["bold"]))
    print(colored("═" * 50 + "\n", "cyan"))

    confirm = input(colored("Bronni tasdiqlaysizmi? (ha/yo'q): ", "magenta"))
    if confirm.lower() != "ha":
        print(colored("❌ Bron bekor qilindi.", "red"))
        return

    booking_id = get_new_id(bookings_list)
    new_booking = {
        "id": booking_id,
        "user_id": user_id,
        "room_id": selected_room["id"],
        "room_number": selected_room["number"],
        "check_in": check_in,
        "check_out": check_out,
        "days": days,
        "total_price": total_price,
        "status": "Faol",
    }

    bookings_list.append(new_booking)
    save_data("data/bookings.json", bookings_list)

    for room in rooms:
        if room["id"] == selected_room["id"]:
            room["status"] = "Band"
            break
    save_data("data/rooms.json", rooms)

    print(colored("\n✔ Bron muvaffaqiyatli yaratildi!", "green"))


def my_bookings(user_id):
    """Foydalanuvchi bronlarini ko'rsatish"""
    draw_box("Mening bronlarim")
    bookings_list = get_data("data/bookings.json")

    user_bookings = [b for b in bookings_list if b["user_id"] == user_id]

    if not user_bookings:
        print(colored("\nSizda hali bronlar yo'q.", "yellow"))
        return

    print()
    print(
        colored(
            f"{'ID':<5} | {'Xona':<6} | {'Kelish':<12} | {'Ketish':<12} | {'Narx':<15} | {'Holat':<10}",
            "cyan",
            attrs=["bold"],
        )
    )
    print(colored("─" * 80, "cyan"))

    for booking in user_bookings:
        print(
            colored(
                f"{booking['id']:<5} | № {booking['room_number']:<4} | {booking['check_in']:<12} | "
                f"{booking['check_out']:<12} | {booking['total_price']:>10} so'm | {booking['status']:<10}",
                "yellow" if booking["status"] == "Faol" else "red",
            )
        )

    print()
    cancel = input(colored("Bronni bekor qilmoqchimisiz? (ha/yo'q): ", "magenta"))
    if cancel.lower() == "ha":
        cancel_booking(user_id, bookings_list)


def cancel_booking(user_id, bookings_list):
    booking_id = input(
        colored("Bekor qilinadigan bron ID sini kiriting >>> ", "magenta")
    )

    if not booking_id.isdigit():
        print(colored("❌ Noto'g'ri ID!", "red"))
        return

    booking_id = int(booking_id)

    for booking in bookings_list:
        if booking["id"] == booking_id and booking["user_id"] == user_id:
            if booking["status"] == "Bekor qilingan":
                print(colored("❌ Bu bron allaqachon bekor qilingan!", "red"))
                return

            booking["status"] = "Bekor qilingan"

            rooms = get_data("data/rooms.json")
            for room in rooms:
                if room["id"] == booking["room_id"]:
                    room["status"] = "Bo'sh"
                    break
            save_data("data/rooms.json", rooms)

            save_data("data/bookings.json", bookings_list)
            print(colored("\n✔ Bron bekor qilindi!", "green"))
            return

    print(colored("❌ Bunday bron topilmadi!", "red"))


def show_profile(user_id):
    users = get_data("data/users.json")
    draw_box("Profil")

    for user in users:
        if user["id"] == user_id:
            print()
            print(colored("Ism >>> ", "yellow")+ colored(user["first_name"], "magenta"))
            print(colored("Familiya >>> ", "yellow")+ colored(user["last_name"], "magenta"))
            print(colored("Telefon >>> ", "yellow") + colored(user["phone"], "magenta"))
            print(colored("Login >>> : ", "yellow") + colored(user["login"], "magenta"))
            break
