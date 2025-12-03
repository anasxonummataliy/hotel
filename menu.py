from auth import UserDatabase,AuthService

class App:
    def __init__(self):
        self.db = UserDatabase()
        self.auth = AuthService(self.db)
        self.current_user = None

    def main_menu(self):
        while True:
            print("\n1. Ro'yxatdan o'tish")
            print("2. Login")
            print("3. Chiqish")

            choice = int(input('Tanlang: '))

            if choice == 1:
                self.auth.register()

            elif choice == 2:
                while True:
                    user = self.auth.login()
                    if user == 'exit':
                        break

                    if user:
                        self.current_user = user
                        self.user_menu()
                        break
                    else:
                        print("\n Xato! Qaytadan kiriting")

            elif choice == 3:
                print('Dastur tugadi.')
                break

            else:
                print('Noto‘g‘ri tanlov!')

    def user_menu(self):
        while True:
            print("\n--- User menyu ---")
            print("1. Profilni ko'rish")
            print("2. Parolni o'zgartirish")
            print("3. Chiqish")

            choice = int(input('Tanlang: '))

            if choice == 1:
                self.show_profile()

            elif choice == 2:
                new_pass = input('Yangi parol: ')
                self.current_user.set_parol(new_pass)
                self.db.save_data()
                print("Parol o'zgartirildi.")

            elif choice == 3:
                self.current_user = None
                break

            else:
                print('Noto‘g‘ri tanlov!')

    def show_profile(self):
        u = self.current_user
        print("\n--- Profil ---")
        print("Ism:", u.ism())
        print("Familiya:", u.get_familiya())
        print("Telefon:", u.phone())
        print("Login:", u.get_login())


app = App()
app.main_menu()
