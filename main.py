from register import *
from login import *
from admin import *
def main():
    while True:
        print("""
        1 - Ro'yxatdan o'tish
        2 - Tizimga kirish
        3 - Admin
        """)
        try:
            tanlov = input("Tanlovingizni kiriting: ")
            if tanlov == "1":
                register()
            elif tanlov == "2":
                login()
            elif tanlov == "3":
                admin()
            elif tanlov == "0":
                print("Dasturdan chiqdingiz")
                break
            else:
                print("Notogri tanlov")
        except ValueError:
            print("Faqat raqam kiriting")
            
if __name__ == "__main__":
    main()
