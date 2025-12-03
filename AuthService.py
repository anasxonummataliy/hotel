from main import UserDatabase,User
class AuthService:
    def __init__(self, db:UserDatabase):
        self.db = db

    def register(self):
        print(" === Ro'yxatdan o'tish === ")
        ism = input('Ism: ')
        familiya = input('Familiya: ')
        telefon = input('Telefon: ')
        login = input('login: ')

        if self.db.user_exists(login):
            print('Bu login bilan user mavjud!')
            return

        parol = input('Parol: ')

        new_user = User(ism, familiya, telefon, login, parol)
        self.db.add_user(new_user)

        print("Muvafaqqiyatli ro'yxatdan o'tdingiz!")



    def login(self):
        print('\n === Login ===')
        print("\n(Bekor qilish uchun 'exit' deb yozing)")

        login = input('Login: ')

        if login.lower() == 'exit':
            return 'exit'

        parol = input('Parol: ')
        if parol.lower() == 'exit':
            return 'exit'

        user = self.db.user_exists(login)

        if user and user.get_parol() == parol:
            return user

        print('Login yoki parol xato! ')
        return None
