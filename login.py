import json

file_name = "data/user.json"

def login():
    username = int(input("Foydalanuvchi nomi: "))
    password = int(input("Parol: "))

    with open(file_name, "r") as f:
        users = json.load(f)

    for user in users:
        if user["username"] == username and user["password"] == password:
            pass
            return 
    print("Notogri login yoki parol!")