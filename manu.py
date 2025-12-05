import json
import os

file_name = 'data/room.json'


class BaseJSON:
    def read(self):
        if not os.path.exists(file_name):
            return []
        with open(file_name, "r") as f:
            return json.load(f)

    def write(self, data):
        with open(file_name, "w") as f:
            json.dump(data, f, indent=4)


class Menu(BaseJSON):
    def __init__(self):
        self.__rooms = self.read()  
        self._bron = []             
        self.profil = {"ism": "Bekzod", "lvl": "gold"}

    def show_xonalar(self):
        print("\n--- Bo'sh xonalar ---")
        for i, room in enumerate(self.__rooms):
            print(f"{i+1}. {room['nomi']} - {room['narx']} so'm")

    def bron_qilish(self):
        self.show_xonalar()
        tanlov = int(input("Qaysi xonani bron qilasiz? "))
        tanlangan = self.__rooms[tanlov-1]
        self._bron.append(tanlangan)
        print(f"{tanlangan['nomi']} muvaffaqiyatli bron qilindi!")

    def mening_bronlarim(self):
        print("\n--- Mening bronlarim ---")
        if not self._bron:
            print("Hali bron qilmagansiz!")
        else:
            for b in self._bron:
                print(f"- {b['nomi']}")

    def show_profil(self):
        print("\n--- Profil ---")
        print(f"Ism: {self.profil['ism']}")
        print(f"Daraja: {self.profil['lvl']}")


class User(Menu):
    def start(self):
        while True:
            print("""
            ===== Mehmonxona Menu =====
            1 - Xonalar
            2 - Bron qilish
            3 - Mening bronlarim
            4 - Profil
            0 - Chiqish
            """)
            try:
                tanlov = int(input("Tanlov: "))

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
            except ValueError:
                print("Faqat raqam kiriting!")


user = User()
user.start()
