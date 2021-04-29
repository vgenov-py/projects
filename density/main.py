# import requests as req
# import matplotlib.pyplot as plt
import csv
import json
import functools
from models import Municipality
# response = req.get("https://datos.comunidad.madrid/catalogo/dataset/032474a0-bf11-4465-bb92-392052962866/resource/301aed82-339b-4005-ab20-06db41ee7017/download/municipio_comunidad_madrid.json").json()
# with open("municipalities.json", "w", encoding="utf8") as file:
#     json.dump(response, file, ensure_ascii=False)


def get_data():
    with open("municipalities.json", "r", encoding="utf8") as file:
        data = json.load(file)["data"]
        return data

data = get_data()


def mean_density(given_list):
    densities = sum(list(map(lambda mun: mun["densidad_por_km2"], given_list)))
    return densities/len(given_list)




def top_10_densidad(given_list):
    lista_densidad=[]
    # lista_densidad=list(sorted(map(lambda mun: mun["densidad_por_km2"], given_list), reverse=True))
    lista_densidad=sorted(list(map(lambda mun: mun["densidad_por_km2"], given_list)), reverse=True)[0:10]
    resultado = list(filter(lambda mun: mun["densidad_por_km2"] in lista_densidad, given_list))

    lista_top=[]
    for dens in lista_densidad[0:10]:
        for mun in given_list:
            if mun["densidad_por_km2"] == dens:
                lista_top.append(mun)
    return resultado

resultado = top_10_densidad(data)
# print(resultado)

def benford(given_list):
    result = []
    for num in range(1,10):
        result.append(len(list(filter(lambda mun: str(mun["densidad_por_km2"]).startswith(str(num)), given_list)))/len(given_list))
    return result

# benford_v = benford(data)
# plt.plot(benford_v)
# plt.show()
# print(benford_v)
# test = mean_density(data)
# print(test)

# def get_biggest(given_list):
#     result = None
#     top = 0
#     for mun in given_list:
#         if mun["superficie_km2"] >= top:
#             top = mun["superficie_km2"]
#             result = mun
#     return result

def get_biggest(given_list):
    areas = map(lambda mun: mun["superficie_km2"],given_list)
    limit = 0
    biggest_area = None
    for area in areas:
        if area >= limit:
            biggest_area = area
            limit = area
    mun_biggest = filter(lambda mun: mun["superficie_km2"] == biggest_area, given_list)
    return next(mun_biggest)

the_biggest = get_biggest(data)

# EJERCICIO 6:

def create_obj_mun(municipality):
    result = Municipality(municipality["municipio_nombre"], municipality["densidad_por_km2"], municipality["superficie_km2"])
    return result
# print(type(test.area))
# print(test.name)
# EJERCICIO 8:

def all_to_objects(dataset):
    result = tuple(map(lambda mun: create_obj_mun(mun),dataset))
    return result

mun_objs = all_to_objects(data)
# print(mun_objs)
# print(mun_objs[0].__str__())

# EJERCICIO 10:
def total_pop(dataset):
    contador = 0

    # CLÁSICA:

    # for mun in dataset:
    #     contador += mun.get_population()
    # return contador
    
    # MAPEO:

    # contador += map(lambda mun: mun.get_population(),dataset)
    resultado = sum(list(map(lambda mun: mun.get_population(),dataset)))
    populations = map(lambda mun: mun.get_population(),dataset)
    for pop_total in populations:
        contador += pop_total
    # return contador
    # return resultado
    # populations = map(lambda mun: mun.get_population(),dataset)

    populations = map(lambda mun: mun.get_population(),dataset)
    resultado = functools.reduce(lambda mun1, mun2: mun1 +  mun2,populations)
    return resultado

# total_population = total_pop(mun_objs)
# print(total_population)
# print(Municipality.population)

acebeda = create_obj_mun(data[0])
# print(acebeda.population)
acebeda.density = 4 
# print(Municipality.total_population)
    
#EJERCICIO 12:
def from_str(value):
    name, density, area = value.split("-")
    return Municipality(name,int(density),int(area))

ej_12 = Municipality.from_str("Madrid-1-2")
# print(ej_12)

# prueba:
a = Municipality.from_str("elobjeto1-23-21")
print(a)

# 1980-1990 1%
a.apply_growth()
print(Municipality.annual_growth_rate)
# print(a)

# 1990-2000 3%
Municipality.set_annual_growth_rate(1.03)
a.apply_growth()
print(Municipality.annual_growth_rate)
# print(a)

# 2000-2010 4%
Municipality.set_annual_growth_rate(1.04)
a.apply_growth()
print(Municipality.annual_growth_rate)
# print(a)

b = Municipality.from_str("elobjeto2-a-32")

print(a.cualquiercosa())


with open("munipalities.csv", "w", newline="", encoding="utf8") as file:
    csv_writer = csv.writer(file,  delimiter= ",")
    csv_writer.writerow(["name","density","area","population"])
    for dea in mun_objs:
        if dea:
            csv_writer.writerow([dea.name,dea.density,dea.area,dea.population])
        else:
            continue
