import json
import os

file_name = "data/data.json"

class Data:
    def __init__(self, boshXonalar, bronQilish, meningBronlarim, profilim):
        self.boshXonalar = boshXonalar
        self.bronQilish = bronQilish
        self.meningBronlarim = meningBronlarim
        self.profilim = profilim

    def bosh_xonalar(self):
        if not os.path.exists(file_name):
            with open(file_name, "w") as f:
                json.dump([], f)

        with open(file_name, "r") as f:
            data = json.load(f)
            return data
        
    
class Menu:
    def __init__(self,username,parol):
        self.username=username
        self.parol=parol
        
    
    def korsatish(self):
         print("""
            1 - Bo'sh xonalar
            2 - Bron qilish
            3 - Mening bronlarim
            4 - Profilim
            0 - Chiqish
            """)
        
# class Menu(Data):
#     def start(self):
#         while True:
#             print("""
#             1 - Bo'sh xonalar
#             2 - Bron qilish
#             3 - Mening bronlarim
#             4 - Profilim
#             0 - Chiqish
#             """)
#             try:
#                 tanlov = int(input("Tanlang: "))

#                 if tanlov == 1:
#                     print("Bo'sh xonalar:")
#                     print(self.bosh_xonalar())

#                 elif tanlov == 0:
#                     print("Chiqdingiz")
#                     break

#                 else:
#                     print("Nato'g'ri tanlov! ")
#             except ValueError:
#                 print("Faqat raqam kiriting")
