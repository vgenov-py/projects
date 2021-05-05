import requests as req
import json
import functools
import utm
import math
from models import Dea
from models import User
from geopy import distance
from utm import to_latlon
# 440547,4473344
# a = utm.to_latlon(443123, 4475002, 30, "N")
# print(a)
def write_json(url):
    response = req.get(url).json()
    with open("deas.json", "w", encoding="utf8") as file:
        json.dump(response, file, ensure_ascii = False, indent=4) 
url = "https://datos.comunidad.madrid/catalogo/dataset/35609dd5-9430-4d2e-8198-3eeb277e5282/resource/c38446ec-ace1-4d22-942f-5cc4979d19ed/download/desfibriladores_externos_fuera_ambito_sanitario.json"
# write_json(url)
deas_json = "deas.json"
users_json = "users.json"


def get_data(file_to_open):
    with open(file_to_open, encoding="utf8") as file:
        data = json.load(file)["data"]
        return data
data = get_data(deas_json)
def write_data(lista, fichero):
    with open(fichero, "w", encoding="utf8") as file:
        toappend = {"data": lista}
        json.dump(toappend, file)
def dea_by_id(dea_code):
    return next(filter(lambda dea: dea["codigo_dea"] == dea_code,data))

def change_latlong(dataset):
    result = {"data": []}
    for i,dea in enumerate(dataset):
        print(i)
        try:
            latlong = utm.to_latlon(int(dea["direccion_coordenada_x"]), int(dea["direccion_coordenada_y"]), 30, "N")
        except:
            continue
        dea["direccion_coordenada_x"] = latlong[0]
        dea["direccion_coordenada_y"] = latlong[1]
        result["data"].append(dea)
    with open("deas_latlon.json", "w", encoding="utf8") as file:
        json.dump(result,file,ensure_ascii=False)

# change_latlong(data)

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
    print("3. Admin")
    print("4. Salir")
    print("-----------------")
menu()
user = input("Elija opción: ")

while user.lower() != "q":

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
            print("3. Buscar DEA por radio")
            print("4. Volver atrás")
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
                    userlatlong=utm.to_latlon(user_x,user_y,30,"N")
                    
                    user = User(user_x, user_y)
                    dea, H = user.get_nearest_dea(data)
                    latlong = utm.to_latlon(int(dea["direccion_coordenada_x"]), int(dea["direccion_coordenada_y"]), 30, "N")
                    def get_meters(user_latlong, dea_latlong):
                        return distance.distance(user_latlong, dea_latlong).m
                    distance_meters = get_meters(userlatlong,latlong)
                    print(dea)
                    print(f"https://www.google.com/maps/search/?api=1&query={latlong[0]},{latlong[1]}")
                    print(f"https://www.google.com/maps/dir/{userlatlong[0]},+{userlatlong[1]}/{latlong[0]},{latlong[1]}")
                    print("Usted está a ",distance_meters," metros", "Hipotenusa: ", H)
                    user = input("Elija opción: ")

                elif user == "3":
                    user_x = int(input("Introduzca coordenada X: "))
                    user_y = int(input("Introduzca coordenada Y: "))
                    user_latlong=utm.to_latlon(user_x,user_y,30,"N")
                    # dea_latlong = utm.to_latlon(int(dea["direccion_coordenada_x"]), int(dea["direccion_coordenada_y"]), 30, "N")

                    user = User(user_x, user_y)
                    deas_list = user.get_nearest_by_radio(data, 100)
                    print(f"Se han encontrado {len(deas_list)} D.E.A.s:")
                    all_points = f"https://www.google.com/maps/dir/{user_latlong[0]},+{user_latlong[1]}/"
                    for dea in deas_list:
                        dea_latlong = utm.to_latlon(int(dea["direccion_coordenada_x"]), int(dea["direccion_coordenada_y"]), 30, "N")
                        all_points+=f"{dea_latlong[0]},{dea_latlong[1]}/"
                    print(all_points)
                    sub_menu()
                    user = input("Elija opción: ")
            else:
                print("Usuario o contraseña incorrectos")
                menu()
                user = input("Elija opción: ")
            
    # ADMIN:
    elif user == "3":
        def sub_menu():
            print("-----------------")
            print("1. Agregar DEA")
            print("2. Modificar DEA")
            print("3. Eliminar DEA")
            print("4. Volver atrás")
            print("-----------------")
        sub_menu()
        user = input("Elija opción: ")

        # CREATE DEA

        if user == "1":
            data = get_data(deas_json)
            dea_keys = list(data[0])
            new_dea = {}
            for key in dea_keys:
                print("-----------------")
                new_dea[key] = input(f"{key}--->")
            print(new_dea)
            user = input("Introduzca ID: ")
        
        elif user == "2":
            user = input("Introduzca ID: ")
            data = get_data(deas_json)
            dea_to_change = list(filter(lambda dea: dea["codigo_dea"] == user,data))[0]
            dea_keys = list(dea_to_change)
            print("-----------------")
            print("Elija clave a modificar")
            for i,key in enumerate(dea_keys):
                print(i,".", key)
            print("-----------------")
            user_key = input("Elija opción: ")
            print("-----------------")
            print(dea_to_change[dea_keys[int(user_key)]]) # dea_to_change["direccion_puerta"]
            print("-----------------")
            user = input("Introduzca valor: ")
            dea_to_change[dea_keys[int(user_key)]] = user
            print("DEA modificado")
            print(dea_to_change)
            user = input("Elija opción: ")
        # DELETE DEA
        elif user == "3":
            user = input("Introduzca ID: ")
            data = get_data(deas_json)
            dea_to_delete = dea_by_id(user)
            print("DEA a eliminar -->", dea_to_delete)
            user = input("¿Está seguro que quiere elminarlo? (s/n): ")
            if user.lower() == "s":
                data.remove(dea_to_delete)
                write_data(data, deas_json)
            sub_menu()
            user = input("Elija opción: ")

    else:
        user = "q"

# a = utm.to_latlon(443123, 4475002, 30, "N") ID:2021-54

