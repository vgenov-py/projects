# import requests as req
import matplotlib.pyplot as plt
import json
import functools
# response = req.get("https://datos.comunidad.madrid/catalogo/dataset/032474a0-bf11-4465-bb92-392052962866/resource/301aed82-339b-4005-ab20-06db41ee7017/download/municipio_comunidad_madrid.json").json()
# print(response["data"][0])
# json.dump
# json.load
# json.loads
# json.dumps
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

# def mean_density_traditional(given_list):
#     densities = []
#     for mun in given_list:
#         densities.append(mun["densidad_por_km2"])
#     return sum(densities)/len(given_list)
mean_density("asd")
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

benford_v = benford(data)
plt.plot(benford_v)
plt.show()
print(benford_v)
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
# print(the_biggest)

# def cosa_complicada(given_list, cohorte):
#     areas =  map(lambda mun: mun["superficie_km2"], given_list)
#     result = list(filter(lambda area: area >= cohorte, areas))
#     return result

# a = cosa_complicada(data, 10)
# print(a)

# a = (1,4,3,2)
# # a.sort(reverse=True)
# # c = a.sort()
# # print(c)
# print("a-->",a)
# b = tuple(sorted(a, reverse=False))
# print("b-->",b)