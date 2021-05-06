import requests as req
import json
import csv
import time
import concurrent.futures

url = "https://restcountries.eu/rest/v2/all"

historial = "historial.csv"
# response = req.get(url).json()
# un comentario

# with open("countries.json", "w", encoding="utf8") as file:
#     json.dump(response,file, ensure_ascii=False, indent=4)

def all_flags():
    response = req.get(url).json()
    flags = map(lambda country: country["flag"], response)
    with open("all_flags.csv", "w", newline="") as file:
        csv_writer = csv.writer(file, delimiter= ",")
        for flag in flags:
            csv_writer.writerow([flag])
# all_flags()



def get_data():
    with open("countries.json", encoding="utf8") as file:
        return json.load(file)

def read_csv(file_to_read):
    with open(file_to_read, encoding="utf8") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        return list(csv_reader)

def by_country(country_name):
    response = req.get(f"https://restcountries.eu/rest/v2/name/{country_name}").json()[0]
    return response

def by_region(region):
    response = req.get(f"https://restcountries.eu/rest/v2/region/{region}").json()
    return response

def get_flag(flag, name=False):
    if name:
        response = req.get(flag).content
        with open(f"img/{name}", "wb") as file:
            file.write(response)
    else:
        response = req.get(flag).content
        name = flag.split("/")[-1]
        with open(f"all_flags/{name}", "wb") as file:
            file.write(response)
    print(f"Se ha guardado la bandera de {name}")

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
        with open("historial.csv", "a", newline="", encoding="utf8") as file:
            escritor = csv.writer(file, delimiter=",")
            escritor.writerow(data)
        print(f"{country['name']} con una población de {country['population']} habitantes")
        menu_principal()
        user = choose()
    

    # OPCIÓN 4: HISTORIAL DE BÚSQUEDA

    #Ejercicio 11:
    elif user == "4":
        data = read_csv(historial)
        for country in data:
            print(f"name: {country[0]}\npopulation: {country[3]}")
            print("---------------------------------------------")
        user = input("Desea descargar las banderas de los países del historial? (Y/N): ").lower()
        if user == "y":
            start_without_threading = time.perf_counter()
            for country in data:
                    flag = country[-1]
                    name = flag.split("/")[-1]
                    get_flag(flag, name)
                    print(f"se está descargando la bandera de {country[0]}")

            finish_without_threading = time.perf_counter()
            print(f"Se han descargado {len(data)} banderas SIN Threading {finish_without_threading-start_without_threading} segundos")

            start_with_threading = time.perf_counter()
            with concurrent.futures.ThreadPoolExecutor() as executor:
                for country in data:
                    flag = country[-1]
                    name = flag.split("/")[-1]
                    future = executor.submit(get_flag,flag, name)
                    print(f"se está descargando la bandera de {country[0]}")

            finish_with_threading = time.perf_counter()
            print(f"Se han descargado {len(data)} banderas CON Threading {finish_with_threading-start_with_threading} segundos")
            user = choose()

    # todas las banderas del mundo:   
    elif user == "6":
        flags = read_csv("all_flags.csv")
        start = time.perf_counter()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # for flag in flags:
            #     executor.submit(get_flag, flag[0])

            [executor.submit(get_flag, flag[0]) for flag in flags]

        finish = time.perf_counter()
        print(f"TIEMPO __> {finish-start}")
        user = choose()
