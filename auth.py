<<<<<<< HEAD
from termcolor import colored
from utils import *
from storage import *

FILE_PATH = "users.json"


class User:
    def __init__(self, fullname, phone, login, password):
        self.fullname = fullname
=======
from utils import *
from utils import *
from storage import *

FILE_PATH = "./data/users.json"


class User:
    def __init__(self, first_name, last_name, phone, login, password):
        self.first_name = first_name
        self.last_name = last_name
>>>>>>> origin/main
        self.phone = phone
        self.login = login
        self.__password = password

    @property
    def get_password(self):
        return self.__password

<<<<<<< HEAD
=======
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

>>>>>>> origin/main

def register():
    while True:
        users = get_data(FILE_PATH)
        draw_box("Ro'yhatdan o'tish")
<<<<<<< HEAD
        fullname = input(colored("Ism-familiya: ", "magenta"))
        phone = input(colored("Telefon: ", "magenta"))
        while True:
            login = input(colored("Login : ", "magenta"))
=======
        first_name = input(colored("Ism >>> ", "magenta"))
        last_name = input(colored("Familiya >>> ", "magenta"))
        while True:
            phone = input(colored("Telefon(exp: +998940581306) >>>", "magenta"))
            if phone.startswith('+998') and len(phone) == 13:
                break
            else:
                print(colored("Noto'g'ri formatda kiritdingiz.\nIltimos qayta kiriting❗️", 'red'))

        while True:
            login = input(colored("Login >>> ", "magenta"))
>>>>>>> origin/main
            flag = False
            if len(login) < 6:
                print(colored("❌ Login kamida 6 ta belgi bo'lishi kerak!", "red"))
            else:
                for user in users:
                    if login == user["login"]:
                        flag = True
                if flag:
                    print(
                        colored(
                            "Bunday foydalanuvchi mavjud, Iltimos boshqa login kiriting❗️",
                            "red",
                        )
                    )
                else:
                    break

        while True:
<<<<<<< HEAD
            password = input(colored("Parol: ", "magenta"))
            if len(password) < 6:
=======
            password = input(colored("Parol >>> ", "magenta"))
            if len(password) < 5:
>>>>>>> origin/main
                print(colored("❌ Parol kamida 6 ta belgi bo'lishi kerak!", "red"))
            else:
                break

<<<<<<< HEAD
        new_user = User(fullname, phone, login, password)

        new_user_data = {
            "id": get_new_id(users),
            "fullname": new_user.fullname,
=======
        new_user = User(first_name, last_name, phone, login, password)
        user_id = get_new_id(users)
        new_user_data = {
            "id": user_id,
            "first_name": new_user.first_name,
            "last_name": new_user.last_name,
>>>>>>> origin/main
            "phone": new_user.phone,
            "login": new_user.login,
            "password": new_user.get_password,
        }
<<<<<<< HEAD

        users.append(new_user_data)
        save_data(FILE_PATH, users)
        return 
=======
        users.append(new_user_data)
        save_data(FILE_PATH, users)
        return user_id
>>>>>>> origin/main


def login():
    while True:
        clear_console()
        users = get_data(FILE_PATH)
        draw_box("Tizimga kirish!")
        while True:
<<<<<<< HEAD
            log = input(colored("Login: ", "magenta"))
=======
            log = input(colored("Login >>> ", "magenta"))
>>>>>>> origin/main
            if len(log) < 6:
                print(colored("❌ Login kamida 6 ta belgi bo'lishi kerak!", "red"))
            else:
                break
        while True:
<<<<<<< HEAD
            password = input(colored("Parol: ", "magenta"))
=======
            password = input(colored("Parol >>> ", "magenta"))
>>>>>>> origin/main
            if len(password) < 6:
                print(colored("❌ Parol kamida 6 ta belgi bo'lishi kerak!", "red"))
            else:
                break

        for user in users:
            if user["login"] == log and user["password"] == password:
                clear_console()
<<<<<<< HEAD
                print(colored(f"✔ Xush kelibsiz, {user['fullname']}!", "green"))
                return 

        print(colored("❌ Login yoki parol noto'g'ri!", "red"))


class Admin:
    pass
=======
                print(colored(f"✔ Xush kelibsiz, {user['fist_name']}!", "green"))
                return

        print(colored("❌ Login yoki parol noto'g'ri!", "red"))

>>>>>>> origin/main
