import json
from foydalanuvchi import Menu

file_name = "data/user.json"

def login():
    try:
        username = input("Foydalanuvchi nomi: ")
        password = input("Parol: ")

        with open(file_name, "r") as f:
            users = json.load(f)

        for user in users:
            if user["username"] == username and user["password"] == password:
                Menu
                return 
        print("Notogri login yoki parol!")
    except ValueError:
        print("To'gri ma'lumot kiriting ")