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
            tanlov = int(input("Tanlovingizni kiriting: "))
            if tanlov == 1:
                register()
            elif tanlov == 2:
                login()
            elif tanlov == 3:
                admin()
            else:
                print("Notogri tanlov")
        except ValueError:
            print("Faqat raqam kiriting")
            
if __name__ == "__main__":
    main()
