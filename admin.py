import json


file_name = "data/user.json"


def admin():
    login = int(input("Login kiriting: "))
    password = int(input("Parolni kiriting: "))

    if login == "admin" and password == "admin12345":
        while True:
            tanlov = input("""
            1 - Xonalar
            2 - Barcha bronlar
            3 - Hisobot
            4 - Mijozlar ro'yhati
            0 - Chiqish
            Tanlov: """)
            if tanlov == 1:
                pass 
            elif tanlov == 5:
                with open(file_name, "r") as f:
                    users = json.load(f)
                    for user in users:
                        print(f"{user['username']}")
            elif tanlov == 3:
                pass
            
            elif tanlov == 0:
                print("Admin paneldan chiqdingiz.")
                break
            else:
                print("Notogri tanlov")
    else:
        print("Login yoki parol xato!")
        