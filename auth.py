from utils import *
from utils import *
from storage import *

FILE_PATH = "./data/users.json"


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
    login = input(colored("Login: ", 'magenta'))
    password = input(colored("Parol: ", 'magenta'))

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

def login():
    users = get_data(FILE_PATH)
    login = input(colored("Login >>> ", 'magenta'))
    password = input(colored("Parol >>> ", 'magenta'))



class Admin:
    pass
