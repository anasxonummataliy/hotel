import json

class User:
    File_user = 'user.json'

    def __init__(self,name, familiya, telefon, login, parol):
        self.name= name
        self.familiya = familiya
        self.telefon = telefon
        self.__login = login
        self.__parol = parol

    def get_login(self):
        return self.__login

    def get_parol(self):
        return self.__parol

    def ism(self):
        return self.name

    def get_familiya(self):
        return self.familiya

    def phone(self):
        return self.telefon

    def set_parol(self, new_pass):
        self.__parol = new_pass

    def to_dict(self):
        return {
            'ism': self.name,
            'familiya': self.familiya,
            'telefon': self.telefon,
            'login': self.__login,
            'parol':self.__parol
        }

    @staticmethod
    def from_dict(data):
        return User(
            data['ism'],
            data['familiya'],
            data['telefon'],
            data['login'],
            data['parol']
        )


class UserDatabase:
    File_user = 'user.json'

    def __init__(self):
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(User.File_user, 'r')as f:
                data = json.load(f)
                return [User.from_dict(u) for u in data]
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_data(self):
        with open(User.File_user, 'w')as f:
            json.dump([u.to_dict() for u in self.users], f, indent=4)

    def user_exists(self, login):
        for i in self.users:
            if i.get_login() == login:
                return i
        return None

    def add_user(self, user):
        self.users.append(user)
        self.save_data()

    def get_user(self, login):
        for u in self.users:
            if u.get_login() == login:
                return u
        return None


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

