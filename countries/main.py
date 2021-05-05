import requests as req
import json
import csv
import time
url = "https://restcountries.eu/rest/v2/all"
# response = req.get(url).json()

# with open("countries.json", "w", encoding="utf8") as file:
#     json.dump(response,file, ensure_ascii=False, indent=4)

def get_data():
    with open("countries.json", encoding="utf8") as file:
        return json.load(file)

# data = get_data()
def menu_principal():
    print("-------------------")
    print("1_Buscar país")
    print("2_Buscar continente")
    print("3_Salir")
    print("-------------------")

menu_principal()
def choose():
    return input("Elija opción: ")

user = choose()
while user != "q":
    # BUSCAR POR PAÍS:
    if user == "3":
        user = "q"
    elif user == "1":
        user = input("Introduzca país: ")
        country = req.get(f"https://restcountries.eu/rest/v2/name/{user}").json()[0]        
        print("Espere se está procesando su respuesta")
        data = [country["name"], country["capital"]]
        with open("historial.csv", "a") as file:
            escritor = csv.writer(file)
            escritor.writerow(data)
        print(f"{country['name']} con una población de {country['population']} habitantes")
        menu_principal()
        user = choose()


