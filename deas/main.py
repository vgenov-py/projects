import requests as req
import json
import functools
from models import Dea
from models import User
def write_json(url):
    response = req.get(url).json()
    with open("deas.json", "w", encoding="utf8") as file:
        json.dump(response, file, ensure_ascii = False, indent=4)
url = "https://datos.comunidad.madrid/catalogo/dataset/35609dd5-9430-4d2e-8198-3eeb277e5282/resource/c38446ec-ace1-4d22-942f-5cc4979d19ed/download/desfibriladores_externos_fuera_ambito_sanitario.json"
# write_json(url)

def get_data():
    with open("deas.json", encoding="utf8") as file:
        data = json.load(file)["data"]
        return data

data = get_data()

def get_title(given, title):
        counter = 0
        for dea in given:
            counter += 1 if dea["tipo_titularidad"] == title else 0
        return counter

def get_inside_M30(given):
    target =("28029", "28036", "28046", "28039", "28016", "28020", "28002", "28003",
    "28015", "28010", "28006", "28028", "28008", "28004", "28001", "280013", "28014",
    "28009", "28007", "28012", "28005", "28045")
    counter = 0
    for dea in given:
        counter += 1 if dea["direccion_codigo_postal"] in target else 0
    return counter

# user = User(439653, 4465806)
# test = user.get_nearest_dea(data[0:1])
# print(test)

def menu():
    print("-----------------")
    print("DEA")
    print("1. Crear usuario")
    print("2. Acceder")
    print("Salir")
    print("-----------------")
menu()
user = input("Elija opción: ")

while user.lower() != "salir":

    # CREAR USUARIO
    if user == "1":
        name = input("Nombre: ")
        password = input("Contraseña: ")
        new_user = {"name": name, "password": password}
        def get_users():
            with open("users.json") as file:
                users = json.load(file)
                return users
        users = get_users()
        users["data"].append(new_user)
        with open("users.json", "w") as file:
            json.dump(users ,file)
        menu()
        user = input(": ")

    # ACCEDER
    elif user == "2":
        def sub_menu():
            print("-----------------")
            print("1. Buscar DEA por código")
            print("2. Buscar DEA por distancia")
            print("3. Volver atrás")
            print("-----------------")

        def by_code(code):
            filter_applied = filter(lambda dea: dea["codigo_dea"]==code, data)
            dea = next(filter_applied, "No encontrado")
            print(dea)
            sub_menu()
            user = input("Elija opción: ")
        

        name = input("Nombre: ")
        password = input("Contraseña: ")
        with open("users.json") as file:
            users = json.load(file)["data"]
            validation = map(lambda user: True if user["name"] == name and user["password"] == password else False, users)
            if next(validation):
                sub_menu()
                user = input("Elija opción: ")

                # DEA POR CÓDIGO
                if user == "1":
                    code = input("Introduzca código: ")
                    by_code(code)
                    sub_menu()
                    user = input("Elija opción: ")

                # DEA POR DISTANCIA
                elif user == "2":
                    user_x = int(input("Introduzca coordenada X: "))
                    user_y = int(input("Introduzca coordenada Y: "))
                    user = User(user_x, user_y)
                    dea = user.get_nearest_dea(data[0:10])
                    print(dea)
                    user = input("Elija opción: ")
            else:
                print("Usuario o contraseña incorrectos")
                menu()
                user = input("Elija opción: ")

