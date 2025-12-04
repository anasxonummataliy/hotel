from termcolor import colored
from utils import *
from storage import *

FILE_PATH = "users.json"


class User:
    def __init__(self, fullname, phone, login, password):
        self.fullname = fullname
        self.phone = phone
        self.login = login
        self.__password = password

    @property
    def get_password(self):
        return self.__password


def register():
    users = get_data(FILE_PATH)
    draw_box("Ro'yhatdan o'tish")
    fullname = input(colored("Ism-familiya: ", 'magenta'))
    phone = input(colored("Telefon: ", 'magenta'))
    while True:
        login = input(colored("Login (kamida 6 ta belgi): ", 'magenta'))
        if len(login) < 6:
            print(colored('Login juda qisqa!', 'red'))
        else:
            break

    while True:
        password = input(colored("Parol: ", 'magenta'))
        if len(password) < 6:
            print(colored('Parol juda qisqa!', 'red'))
        else:
            break

    new_user = User(fullname, phone, login, password)


    new_user_data = {
        'id': get_new_id(users),
        "fullname": new_user.fullname,
        "phone": new_user.phone,
        "login": new_user.login,
        'password': new_user.get_password
    }

    users.append(new_user_data)
    save_data(FILE_PATH, users)
    return True

def login():
    users = get_data(FILE_PATH)
    draw_box("Tizimga kirish!")

    while True:
        log = input(colored("Login: ", 'magenta'))
        if len(log) < 6:
            print(colored("❌ Login kamida 6 ta belgi bo'lishi kerak!", "red"))
        else:
            break

    while True:
        password = input(colored("Parol: ", "cyan"))
        if len(password) < 6:
            print(colored("❌ Parol kamida 6 ta belgi bo'lishi kerak!", "red"))
        else:
            break

    for user in users:
        if user['login'] == log and user['password'] == password:
            print(colored(f"✔ Xush kelibsiz, {user['fullname']}!", 'green'))
            return True

    print(colored("❌ Login yoki parol noto'g'ri!", 'red'))
    return False

class Admin:
    pass