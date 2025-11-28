import json
import os



file_name = "data/user.json"
file_name2 = "data/xona.json"

if not os.path.exists(file_name):
    with open(file_name, "w") as f:
        json.dump([], f)


def register():
    username = int(input("Foydalanuvchi nomini kiriting: "))
    password = int(input("Parol kiriting: "))

    with open(file_name, "r") as f:
        users = json.load(f)

    for user in users:
        if user["username"] == username:
            print("Bu foydalanuvchi allaqachon mavjud!")
            return

    users.append({"username": username, "password": password})

    with open(file_name, "w") as f:
        json.dump(users, f, indent=4)

    print("Muvaffaqiyatli ro'yxatdan o'tdingiz")
