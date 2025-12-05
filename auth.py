from utils import *
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
    users = get_data(FILE_PATH)
    draw_box("Ro'yhatdan o'tish")
    first_name = input(colored("Ism: ", "magenta"))
    last_name = input(colored("Familiya: ", "magenta"))
    phone = input(colored("Telefon: ", "magenta"))
    login = input(colored("Login: ", "magenta"))
    password = input(colored("Parol: ", "magenta"))

    new_user = User(first_name, last_name, phone, login, password)
    new_user_data = {
        "id": get_new_id(users),
        "first_name": new_user.first_name,
        "last_name": new_user.last_name,
        "phone": new_user.phone,
        "login": new_user.login,
        "password": new_user.get_password,
    }

    users.append(new_user_data)
    save_data(FILE_PATH, users)


def login():
    users = get_data(FILE_PATH)
    login = input(colored("Login >>> ", "magenta"))
    password = input(colored("Parol >>> ", "magenta"))


class Admin:
    pass
