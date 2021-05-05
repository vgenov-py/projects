import requests as req
import json
import csv
import time
import concurrent.futures

url = "https://restcountries.eu/rest/v2/all"
# response = req.get(url).json()

# with open("countries.json", "w", encoding="utf8") as file:
#     json.dump(response,file, ensure_ascii=False, indent=4)

def get_data():
    with open("countries.json", encoding="utf8") as file:
        return json.load(file)

def by_country(country_name):
    response = req.get(f"https://restcountries.eu/rest/v2/name/{country_name}").json()[0]
    return response

def by_region(region):
    response = req.get(f"https://restcountries.eu/rest/v2/region/{region}").json()
    return response

busqueda = by_country("argentina")
print(busqueda["name"])
# data = get_data()
def menu_principal():
    print("-------------------")
    print("1. Buscar país")
    print("2. Buscar continente")
    print("3. Population")
    print("4. Historial")
    print("5. Salir")
    print("-------------------")

menu_principal()
def choose():
    return input("Elija opción: ")

user = choose()
while user != "q":
    # BUSCAR POR PAÍS:
    if user == "5":
        user = "q"
    elif user == "1":
        user = input("Introduzca país: ")
        with concurrent.futures.ThreadPoolExecutor() as executor:
            f1 = executor.submit(by_country, user)
            print("Espere se está procesando su respuesta") 
            country = f1.result()

        data = [country["name"], country["capital"], country["region"],
                country["population"], country["area"], country["languages"][0]["name"], country["flag"]]
        with open("historial.csv", "a", newline="") as file:
            escritor = csv.writer(file, delimiter=",")
            escritor.writerow(data)
        print(f"{country['name']} con una población de {country['population']} habitantes")
        menu_principal()
        user = choose()


