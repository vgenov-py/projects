import requests as req
import json
import os
import functions as func

# response =req.get("https://datos.comunidad.madrid/catalogo/dataset/35609dd5-9430-4d2e-8198-3eeb277e5282/resource/c38446ec-ace1-4d22-942f-5cc4979d19ed/download/desfibriladores_externos_fuera_ambito_sanitario.json").json()["data"]
# with open("deas.json", "w", encoding="utf8") as file:
#     json.dump(response,file, ensure_ascii=False, indent=4)
di_path = os.path.realpath(__file__)[0:-8]

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


