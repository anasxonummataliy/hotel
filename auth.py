from utils import *
from storage import *

FILE_PATH = "./data/users.json"


class User:
    def __init__(self, first_name, last_name, phone, login, password):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.login = login
        self.__password = password

    @property
    def get_password(self):
        return self.__password

    @get_password.setter
    def set_password(self, new_password):
        if len(new_password) > 5:
            self.__password = new_password
        else:
            print(
                colored(
                    "Parol uzunligi eng kamida 6 ta belgidan iborat bo'lishi kerak.\nIltimos qayta kiriting!",
                    "red",
                )
            )


def register():
    clear_console()
    users = get_data(FILE_PATH)
    draw_box("Ro'yhatdan o'tish")

    first_name = input(colored("Ism >>> ", "magenta"))
    last_name = input(colored("Familiya >>> ", "magenta"))

    while True:
        phone = input(colored("Telefon (exp: +998940581306) >>> ", "magenta"))
        if phone.startswith("+998") and len(phone) == 13 and phone[1:].isdigit():
            break
        else:
            print(colored("❌ Noto'g'ri formatda! Qayta kiriting.", "red"))

    while True:
        login = input(colored("Login >>> ", "magenta"))
        if len(login) < 6:
            print(colored("❌ Login kamida 6 ta belgi bo'lishi kerak!", "red"))
            continue

        if any(user["login"] == login for user in users):
            print(colored("❌ Bu login band! Boshqa login kiriting.", "red"))
        else:
            break

    while True:
        password = input(colored("Parol >>> ", "magenta"))
        if len(password) < 6:
            print(colored("❌ Parol kamida 6 ta belgi bo'lishi kerak!", "red"))
        else:
            break

    new_user = User(first_name, last_name, phone, login, password)
    user_id = get_new_id(users)

    new_user_data = {
        "id": user_id,
        "first_name": new_user.first_name,
        "last_name": new_user.last_name,
        "phone": new_user.phone,
        "login": new_user.login,
        "password": new_user.get_password,
    }

    users.append(new_user_data)
    save_data(FILE_PATH, users)

    print(colored(f"\n✔ Muvaffaqiyatli ro'yxatdan o'tdingiz!", "green"))
    show_progres("Tizimga kirilmoqda")
    print()

    return user_id


def login():
    clear_console()
    users = get_data(FILE_PATH)
    draw_box("Tizimga kirish")

    while True:
        log = input(colored("Login >>> ", "magenta"))
        password = input(colored("Parol >>> ", "magenta"))

        for user in users:
            if user["login"] == log and user["password"] == password:
                clear_console()
                print(colored(f"✔ Xush kelibsiz, {user['first_name']}!", "green"))
                show_progres("Yuklanmoqda")
                print()
                return user["id"]  

        print(colored("\n❌ Login yoki parol noto'g'ri!", "red"))
        choice = input(colored("Qayta urinib ko'rasizmi? (ha/yo'q): ", "yellow"))
        if choice.lower() != "ha":
            return None
