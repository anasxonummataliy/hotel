import json
import os

file_name = "data/user.json"

if not os.path.exists(file_name):
    with open(file_name, "w") as f:
        json.dump([], f)


def register():
    username = int(input("Ism kiriting: "))
    familiya = int(input("Familiya kiriting: "))
    telefon = int(input("Telefon kiriting: "))
    password = int(input("Parol kiriting: "))

    with open(file_name, "r") as f:
        users = json.load(f)

    for user in users:
        if user["username"] == username or ["familiya"] == familiya:
            print("Bu foydalanuvchi allaqachon mavjud!")
            return
        elif  user["telefon"] == telefon:
            print("Bu raqam allaqachon mavjud")

    users.append({"username": username, "familiya": familiya, "telefon": telefon, "password": password})

    with open(file_name, "w") as f:
        json.dump(users, f, indent=4)   

    print("Muvaffaqiyatli ro'yxatdan o'tdingiz")
