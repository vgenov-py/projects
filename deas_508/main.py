# import requests as req
import json
import os
import utm
import geocoder
import functions as func

# response =req.get("https://datos.comunidad.madrid/catalogo/dataset/35609dd5-9430-4d2e-8198-3eeb277e5282/resource/c38446ec-ace1-4d22-942f-5cc4979d19ed/download/desfibriladores_externos_fuera_ambito_sanitario.json").json()["data"]
# with open("deas.json", "w", encoding="utf8") as file:
#     json.dump(response,file, ensure_ascii=False, indent=4)
di_path = os.path.realpath(__file__)[0:-8]

g = geocoder.ip('me')
print(g.json)
#  y = "4475002", x = "443123" 
print(utm.to_latlon(443123, 4475002, 30, "N"))
print(utm.from_latlon(0, 0))


def get_data():
    with open(f"{di_path}\deas.json", encoding="utf8") as file:
        return json.load(file)

data = get_data()

func.menu()
user = func.choose()
while user != "4":
    if user == "1":
        print("acceder")
        user = func.choose()
    elif user == "2":
        func.sub_menu_access()
        user = func.choose()
        if user == "1": # Buscar por código
            dea_code = func.choose("Indique el código del DEA: ")
            result = func.dea_by_id(dea_code, data)
            print(result)
            user = func.choose()
        elif user == "2": # DEA más cercano y = "4475002", x = "443123"   Y: 4473337 X: 440561
            user_x = func.choose("Indique coordenada X: ")
            user_y = func.choose("Indique coordenada y: ")
            result, distance = func.nearest_dea(user_x, user_y,data)
            print(f"DEA -->{result}\nDISTANCIA --> {distance}\n Maps-->")
            user = func.choose()