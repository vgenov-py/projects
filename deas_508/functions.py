from models import Dea
import json
import bcrypt
import utm

def menu():
    print("----------------")
    print("1. Crear usuario")
    print("2. Acceder")
    print("3. Admins")
    print("4. Salir")
    print("----------------")

#LECTURA Y ESCRITURA DE FICHEROS JSON:

def read_data(fichero):
    with open(fichero, encoding="utf8") as file:
        return json.load(file)

def write_data(to_write, fichero):
    with open(fichero, "w", encoding="utf8") as file:
        json.dump(to_write, file, indent=4, ensure_ascii=False)
    print("Guardado correctamente")

#1. CREAR USUARIO:
def create_user(name, password):
    new_user = {"name": name, "password": password}
    return new_user

#2. LOGUEAR USUARIO:
def log_in(name, password, fichero):
    users = read_data(fichero)
    is_user = next(filter(lambda user: user["name"] == name,users["data"]), False)
    is_password = is_user["password"] if is_user else False
    veredict = False
    if is_password:
        veredict = True if bcrypt.checkpw(password.encode(), is_password.encode()) else veredict
    return veredict

def choose(msg = "Elija una opción: "):
    return input(msg)

def sub_menu_access():
    print("--------------------")
    print("1. Buscar por código")
    print("2. DEA más cercano")
    print("3. DEA por rápido")
    print("--------------------")

def dea_by_id(dea_code, dataset):
    result = filter(lambda dea: dea["codigo_dea"] == dea_code, dataset)
    return next(result, "El DEA no está")

def nearest_dea(user_x, user_y, dataset):
    user_x = int(user_x)
    user_y = int(user_y)
    result = None
    first_dea = dataset[0]
    coord_x = "direccion_coordenada_x"
    coord_y = "direccion_coordenada_y"
    first_dea_object = Dea(int(first_dea[coord_x]), int(first_dea[coord_y]))
    distance_to_beat = first_dea_object.distance(user_x, user_y)

    for dea in dataset:
        dea_object = Dea(int(dea[coord_x]), int(dea[coord_y]))
        dea_distance = dea_object.distance(user_x, user_y)
        if dea_distance <= distance_to_beat:
            result = dea
            distance_to_beat = dea_distance
        else:
            continue
    return result, distance_to_beat

def top_5_dea(user_x, user_y, dataset, range):
    user_x = int(user_x)
    user_y = int(user_y)
    result = {}
    coord_x = "direccion_coordenada_x"
    coord_y = "direccion_coordenada_y"

    for dea in dataset:
        dea_object = Dea(int(dea[coord_x]), int(dea[coord_y]))
        dea_distance = dea_object.distance(user_x, user_y)
        result[(dea[coord_x], dea[coord_y])] = dea_distance

    result = dict(sorted(result.items(), key = lambda dea: dea[1]))
    for dea in list(result.keys())[0:int(range)]:
        coord_utm = utm.to_latlon(int(dea[0]), int(dea[1]),30, "N")
        print(f"https://www.google.com/maps/search/?api=1&query={coord_utm[0]},{coord_utm[1]}" )