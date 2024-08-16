class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "role": self.role
        }

class Admin(User):
    def __init__(self, username, password, role="Admin"):
        super().__init__(username, password, role)

    def manage_users(self, users, data):
        print("1. Dodaj użytkownika")
        print("2. Usuń użytkownika")
        choice = int(input("Wybierz opcję: "))
        if choice == 1:
            new_username = input("Podaj nazwę użytkownika: ")
            new_password = input("Podaj hasło: ")
            new_role = input("Podaj rolę (Admin/Employee): ")
            users.append(User(new_username, new_password, new_role))
        elif choice == 2:
            del_username = input("Podaj nazwę użytkownika do usunięcia: ")
            users[:] = [user for user in users if user.username != del_username]

class Employee(User):
    def __init__(self, username, password, role="Employee"):
        super().__init__(username, password, role)
