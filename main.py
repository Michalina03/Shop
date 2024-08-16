import json
from users import Admin, Employee
from shop import Shop
from report import generate_report

def load_data():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            "users": [
                {"username": "admin", "password": "admin123", "role": "Admin"},
                {"username": "mike", "password": "mike123", "role": "Employee"},
                {"username": "anna", "password": "anna123", "role": "Employee"}
            ],
            "shop": {
                "products": [
                    {"name": "Doll", "price": 15.0},
                    {"name": "Ball", "price": 10.0},
                    {"name": "Cookies", "price": 5.0}
                ],
                "balance": 150.0
            }
        }

def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

def find_user(users, username, password):
    for user in users:
        if user.username == username and user.password == password:
            return user
    return None

data = load_data()

users = [Admin(**user) if user['role'] == 'Admin' else Employee(**user) for user in data['users']]
shop = Shop(data['shop'])

print("Logowanie do systemu:")
username = input("Podaj nazwę użytkownika: ")
password = input("Podaj hasło: ")

user = find_user(users, username, password)

if not user:
    print("Błędny login lub hasło.")
else:
    print(f"Witaj, {user.username}!")
    if isinstance(user, Admin):
        print("1. Zarządzaj użytkownikami")
        print("2. Zarządzaj sklepem")
    elif isinstance(user, Employee):
        print("1. Sprzedawaj produkt")

    choice = int(input("Wybierz opcję: "))

    if isinstance(user, Admin):
        if choice == 1:
            user.manage_users(users, data)
        elif choice == 2:
            shop.manage_shop()
    elif isinstance(user, Employee):
        if choice == 1:
            shop.sell_product(user)

    save_data({"users": [u.to_dict() for u in users], "shop": shop.to_dict()})
    generate_report(users, shop)
