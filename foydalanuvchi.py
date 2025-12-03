import json
import os

file_name = "data/data.json"

class Data:
    def __init__(self):
        if not os.path.exists(file_name):
            with open(file_name, "w") as f:
                json.dump([], f)

    def bosh_xonalar(self):
        with open(file_name, "r") as f:
            data = json.load(f)
        return data
        
    def bron_qilish(self):
        with open(file_name, "r") as f:
            data = json.load(f)
        return data
    

class Menu(Data):
    def __init__(self, username, parol):
        super().__init__() 
        self.username = username
        self.parol = parol
        
    def korsatish(self):
        print("""
            1 - Bo'sh xonalar
            2 - Bron qilish
            3 - Mening bronlarim
            4 - Profilim
            0 - Chiqish
            """)

        tanlov = input("Tanlov: ")

        if tanlov == "1":
            print(self.bosh_xonalar())
        
        elif tanlov == "2":
            print(self.bron_qilish())
