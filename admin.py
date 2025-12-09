from storage import *
from utils import *
from datetime import datetime


class Admin:
    def __init__(self):
        self._login = "admin"
        self.__password = "admin123"  # Xavfsizlik uchun

    def login(self):
        """Admin tizimga kirish"""
        clear_console()
        draw_box("ADMIN PANEL")

        login = input(colored("\nLogin >>> ", "magenta"))
        password = input(colored("Parol >>> ", "magenta"))

        if login == self._login and password == self.__password:
            print(colored("\n✔ Xush kelibsiz, Admin!", "green"))
            show_progres("Yuklanmoqda")
            print()
            return True
        else:
            print(colored("\n❌ Login yoki parol noto'g'ri!", "red"))
            return False

    def menu(self):
        """Admin menu"""
        while True:
            clear_console()
            draw_box("ADMIN MENU")
            print(colored("1. Xonalar boshqaruvi", "yellow"))
            print(colored("2. Barcha bronlar", "yellow"))
            print(colored("3. Hisobot", "yellow"))
            print(colored("4. Mijozlar ro'yhati", "yellow"))
            print(colored("0. Chiqish", "cyan"))

            choice = input(colored("\nTanlov >>> ", "magenta"))

            match choice:
                case "1":
                    self.rooms_management()
                case "2":
                    clear_console()
                    self.get_all_bookings()
                    input(colored("\nDavom etish uchun Enter...", "cyan"))
                case "3":
                    clear_console()
                    self.show_report()
                    input(colored("\nDavom etish uchun Enter...", "cyan"))
                case "4":
                    clear_console()
                    self.get_all_customers()
                    input(colored("\nDavom etish uchun Enter...", "cyan"))
                case "0":
                    print(colored("\n✔ Xayr! 👋", "green"))
                    return
                case _:
                    print(colored("\n❌ Noto'g'ri tanlov!", "red"))
                    input(colored("Davom etish uchun Enter...", "cyan"))

    def rooms_management(self):
        """Xonalar boshqaruvi menu"""
        while True:
            clear_console()
            draw_box("Xonalar Boshqaruvi")
            print(colored("1. Barcha xonalar", "yellow"))
            print(colored("2. Xona qo'shish", "yellow"))
            print(colored("3. Xona o'chirish", "yellow"))
            print(colored("4. Xona holatini o'zgartirish", "yellow"))
            print(colored("0. Orqaga", "cyan"))

            choice = input(colored("\nTanlov >>> ", "magenta"))

            match choice:
                case "1":
                    clear_console()
                    self.get_all_rooms()
                    input(colored("\nDavom etish uchun Enter...", "cyan"))
                case "2":
                    clear_console()
                    self.add_room()
                    input(colored("\nDavom etish uchun Enter...", "cyan"))
                case "3":
                    clear_console()
                    self.delete_room()
                    input(colored("\nDavom etish uchun Enter...", "cyan"))
                case "4":
                    clear_console()
                    self.update_room_status()
                    input(colored("\nDavom etish uchun Enter...", "cyan"))
                case "0":
                    return
                case _:
                    print(colored("\n❌ Noto'g'ri tanlov!", "red"))
                    input(colored("Davom etish uchun Enter...", "cyan"))

    def get_all_rooms(self):
        """Barcha xonalarni ko'rsatish"""
        rooms = get_data("data/rooms.json")
        draw_box("Barcha Xonalar")
        print()
        print(
            colored(
                f"{'ID':<5} | {'Raqam':<8} | {'Turi':<15} | {'Narxi':<15} | {'Holati':<10}",
                "cyan",
                attrs=["bold"],
            )
        )
        print(colored("─" * 70, "cyan"))

        for room in rooms:
            status_color = "green" if room["status"] == "Bo'sh" else "red"
            print(
                colored(f"{room['id']:<5} | ", "yellow")
                + colored(f"№ {room['number']:<6} | ", "yellow")
                + colored(f"{room['type']:<15} | ", "yellow")
                + colored(f"{room['price']:>10} so'm | ", "yellow")
                + colored(f"{room['status']:<10}", status_color)
            )

    def add_room(self):
        """Yangi xona qo'shish"""
        draw_box("Yangi Xona Qo'shish")
        rooms = get_data("data/rooms.json")

        # Xona raqami
        while True:
            number = input(colored("\nXona raqami >>> ", "magenta"))
            if not number.isdigit():
                print(colored("❌ Faqat raqam kiriting!", "red"))
                continue

            number = int(number)
            if any(room["number"] == number for room in rooms):
                print(colored("❌ Bu raqamdagi xona mavjud!", "red"))
                continue
            break

        # Xona turi
        print(colored("\nXona turlari:", "cyan"))
        print(colored("1. Standart", "yellow"))
        print(colored("2. Lux", "yellow"))
        print(colored("3. VIP", "yellow"))

        type_choice = input(colored("Tanlov >>> ", "magenta"))
        room_types = {
            "1": ("Standart", 300000),
            "2": ("Lux", 500000),
            "3": ("VIP", 1000000),
        }

        if type_choice not in room_types:
            print(colored("❌ Noto'g'ri tanlov!", "red"))
            return

        room_type, default_price = room_types[type_choice]

        # Narx
        price_input = input(
            colored(f"Narx (standart: {default_price:,} so'm) >>> ", "magenta")
        )
        price = int(price_input) if price_input.isdigit() else default_price

        # Yangi xona
        room_id = get_new_id(rooms)
        new_room = {
            "id": room_id,
            "number": number,
            "type": room_type,
            "price": price,
            "status": "Bo'sh",
        }

        rooms.append(new_room)
        save_data("data/rooms.json", rooms)

        print(colored("\n✔ Xona muvaffaqiyatli qo'shildi!", "green"))

    def delete_room(self):
        """Xonani o'chirish"""
        self.get_all_rooms()

        room_id = input(colored("\nO'chiriladigan xona ID si >>> ", "magenta"))
        if not room_id.isdigit():
            print(colored("❌ Noto'g'ri ID!", "red"))
            return

        room_id = int(room_id)
        rooms = get_data("data/rooms.json")

        for room in rooms:
            if room["id"] == room_id:
                if room["status"] == "Band":
                    print(colored("❌ Band xonani o'chirib bo'lmaydi!", "red"))
                    return

                confirm = input(
                    colored(
                        f"№ {room['number']} xonani o'chirasizmi? (ha/yo'q): ", "yellow"
                    )
                )
                if confirm.lower() == "ha":
                    rooms.remove(room)
                    save_data("data/rooms.json", rooms)
                    print(colored("\n✔ Xona o'chirildi!", "green"))
                return

        print(colored("❌ Xona topilmadi!", "red"))

    def update_room_status(self):
        """Xona holatini o'zgartirish"""
        self.get_all_rooms()

        room_id = input(colored("\nXona ID si >>> ", "magenta"))
        if not room_id.isdigit():
            print(colored("❌ Noto'g'ri ID!", "red"))
            return

        room_id = int(room_id)
        rooms = get_data("data/rooms.json")

        for room in rooms:
            if room["id"] == room_id:
                print(colored("\n1. Bo'sh", "green"))
                print(colored("2. Band", "red"))

                status_choice = input(colored("Yangi holat >>> ", "magenta"))
                new_status = (
                    "Bo'sh"
                    if status_choice == "1"
                    else "Band" if status_choice == "2" else None
                )

                if new_status:
                    room["status"] = new_status
                    save_data("data/rooms.json", rooms)
                    print(colored("\n✔ Holat o'zgartirildi!", "green"))
                return

        print(colored("❌ Xona topilmadi!", "red"))

    def get_all_bookings(self):
        """Barcha bronlarni ko'rsatish"""
        draw_box("Barcha Bronlar")
        bookings = get_data("data/bookings.json")

        if not bookings:
            print(colored("\nHali bronlar yo'q.", "yellow"))
            return

        print()
        print(
            colored(
                f"{'ID':<5} | {'Mijoz':<8} | {'Xona':<6} | {'Kelish':<12} | {'Ketish':<12} | {'Narx':<15} | {'Holat':<12}",
                "cyan",
                attrs=["bold"],
            )
        )
        print(colored("─" * 95, "cyan"))

        for booking in bookings:
            status_color = "green" if booking["status"] == "Faol" else "red"
            print(
                colored(f"{booking['id']:<5} | ", "yellow")
                + colored(f"ID: {booking['user_id']:<4} | ", "yellow")
                + colored(f"№ {booking['room_number']:<4} | ", "yellow")
                + colored(f"{booking['check_in']:<12} | ", "yellow")
                + colored(f"{booking['check_out']:<12} | ", "yellow")
                + colored(f"{booking['total_price']:>10} so'm | ", "yellow")
                + colored(f"{booking['status']:<12}", status_color)
            )

    def show_report(self):
        """Hisobot ko'rsatish"""
        draw_box("Hisobot")

        rooms = get_data("data/rooms.json")
        bookings = get_data("data/bookings.json")

        # Xonalar statistikasi
        total_rooms = len(rooms)
        available_rooms = sum(1 for room in rooms if room["status"] == "Bo'sh")
        occupied_rooms = total_rooms - available_rooms

        # Bronlar statistikasi
        active_bookings = sum(1 for b in bookings if b["status"] == "Faol")
        cancelled_bookings = sum(1 for b in bookings if b["status"] == "Bekor qilingan")
        total_income = sum(b["total_price"] for b in bookings if b["status"] == "Faol")

        # Bugungi bronlar
        today = datetime.now().strftime("%Y-%m-%d")
        today_bookings = sum(
            1 for b in bookings if b["check_in"] == today and b["status"] == "Faol"
        )

        print()
        print(colored("═" * 50, "cyan"))
        print(colored(" XONALAR STATISTIKASI", "green", attrs=["bold"]))
        print(colored("═" * 50, "cyan"))
        print(colored(f"Jami xonalar      : {total_rooms}", "yellow"))
        print(colored(f"Bo'sh xonalar     : {available_rooms}", "green"))
        print(colored(f"Band xonalar      : {occupied_rooms}", "red"))

        print()
        print(colored("═" * 50, "cyan"))
        print(colored(" BRONLAR STATISTIKASI", "green", attrs=["bold"]))
        print(colored("═" * 50, "cyan"))
        print(colored(f"Faol bronlar      : {active_bookings}", "green"))
        print(colored(f"Bekor qilingan    : {cancelled_bookings}", "red"))
        print(colored(f"Bugungi bronlar   : {today_bookings}", "yellow"))

        print()
        print(colored("═" * 50, "cyan"))
        print(colored(" MOLIYAVIY STATISTIKA", "green", attrs=["bold"]))
        print(colored("═" * 50, "cyan"))
        print(
            colored(
                f"Jami daromad      : {total_income:,} so'm", "green", attrs=["bold"]
            )
        )
        print(colored("═" * 50, "cyan"))

    def get_all_customers(self):
        """Barcha mijozlarni ko'rsatish"""
        draw_box("Mijozlar Ro'yhati")
        users = get_data("data/users.json")

        if not users:
            print(colored("\nHali mijozlar yo'q.", "yellow"))
            return

        print()
        print(
            colored(
                f"{'ID':<5} | {'Ism':<15} | {'Familiya':<15} | {'Telefon':<15} | {'Login':<15}",
                "cyan",
                attrs=["bold"],
            )
        )
        print(colored("─" * 80, "cyan"))

        for user in users:
            print(
                colored(
                    f"{user['id']:<5} | {user['first_name']:<15} | {user['last_name']:<15} | "
                    f"{user['phone']:<15} | {user['login']:<15}",
                    "yellow",
                )
            )


def admin():
    admin_obj = Admin()
    if admin_obj.login():
        admin_obj.menu()
