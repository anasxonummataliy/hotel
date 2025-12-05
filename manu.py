import json
import os
from datetime import datetime

rooms_file = 'data/room.json'
bookings_file = 'data/bookings.json'
current_user_id = 1

class BaseJSON:
    def read(self, file_name):
        if not os.path.exists(file_name):
            return []
        with open(file_name, 'r') as f:
            return json.load(f)

    def write(self, file_name, data):
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=4)

class Menu(BaseJSON):
    def __init__(self):
        self.rooms = self.read(rooms_file)
        self.bookings = self.read(bookings_file)
        self.profil = {"id": current_user_id, "ism": "Bekzod", "lvl": "Gold"}

    def show_xonalar(self):
        for i, room in enumerate(self.rooms, 1):
            print(f"{i}. Xona {room['number']} | {room['type']} | {room['price']} so'm | {room['status']}")

    def show_available_rooms(self):
        for i, room in enumerate(self.rooms, 1):
            if room['status'] == 'Available':
                print(f"{i}. Xona {room['number']} | {room['type']} | {room['price']} so'm")

    def bron_qilish(self):
        self.show_available_rooms()
        try:
            tanlov = int(input("Qaysi xonani bron qilasiz? (raqam kiriting): "))
        except ValueError:
            print("Raqam kiriting!")
            return

        available_rooms = [r for r in self.rooms if r['status'] == 'Available']
        if tanlov < 1 or tanlov > len(available_rooms):
            print("Noto'g'ri tanlov!")
            return

        tanlangan = available_rooms[tanlov-1]

        check_in = input("Check-in sanasini kiriting (YYYY-MM-DD): ")
        check_out = input("Check-out sanasini kiriting (YYYY-MM-DD): ")

        try:
            date_in = datetime.strptime(check_in, "%Y-%m-%d")
            date_out = datetime.strptime(check_out, "%Y-%m-%d")
            if date_out <= date_in:
                print("Check-out sanasi check-in sanasidan oldin bo'lishi mumkin emas!")
                return
        except:
            print("Sanani YYYY-MM-DD formatida kiriting!")
            return

        total_days = (date_out - date_in).days
        total_price = total_days * tanlangan['price']

        booking_id = 1
        if self.bookings:
            booking_id = max(b['id'] for b in self.bookings) + 1

        new_booking = {
            "id": booking_id,
            "user_id": self.profil["id"],
            "room_id": tanlangan["id"],
            "check_in": check_in,
            "check_out": check_out,
            "total_price": total_price,
            "status": "Pending"
        }

        self.bookings.append(new_booking)
        self.write(bookings_file, self.bookings)

        tanlangan['status'] = 'Occupied'
        self.write(rooms_file, self.rooms)

        print(f"Xona {tanlangan['number']} muvaffaqiyatli bron qilindi!")
        print(f"Umumiy narx: {total_price} so'm. Status: Pending")

    def mening_bronlarim(self):
        user_bookings = [b for b in self.bookings if b['user_id'] == self.profil["id"]]
        if not user_bookings:
            print("Hali bron qilmagansiz.")
        else:
            for b in user_bookings:
                room = next(r for r in self.rooms if r['id'] == b['room_id'])
                print(f"- Xona {room['number']} | {room['type']} | {b['check_in']} -> {b['check_out']} | {b['total_price']} so'm | {b['status']}")

    def show_profil(self):
        print(f"Ism: {self.profil['ism']}")
        print(f"Daraja: {self.profil['lvl']}")

class User(Menu):
    def start(self):
        while True:
            print("""
===== Mehmonxona Menu =====
1 - Barcha xonalar
2 - Bron qilish
3 - Mening bronlarim
4 - Profil
0 - Chiqish
""")
            try:
                tanlov = int(input("Tanlov: "))
            except ValueError:
                print("Faqat raqam kiriting!")
                continue

            if tanlov == 1:
                self.show_xonalar()
            elif tanlov == 2:
                self.bron_qilish()
            elif tanlov == 3:
                self.mening_bronlarim()
            elif tanlov == 4:
                self.show_profil()
            elif tanlov == 0:
                print("Dastur tugadi.")
                break
            else:
                print("Noto'g'ri tanlov!")

user = User()
user.start()
