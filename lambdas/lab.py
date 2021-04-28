import requests as req
from functools import reduce
# response = req.get("https://raw.githubusercontent.com/vgenov-py/projects/master/deas/deas_latlon.json").json()
# print(response["data"][0])

# a = 1
# def greeting():
#     print("Hola!")

# greeting()
# def lafuncion():
#     pass

# matematica = {"suma": lambda a,b: a+b, "resta": lambda a,b: a-b, "cuadrado": lambda a: a**2}
# resultado = matematica["cuadrado"](2)
# print(resultado)
# a = 2
# def cuadrados(num):
#     return num **2

# cuadrado_lambda = lambda num:num**2
# resultado = cuadrado_lambda(a)
# print(resultado)

# a = [1,2,3,4]
# b = map(lambda num: num, a)
# for num in b:
#     print(num)


# def cuadrado(num):
#     return num ** 2
# resultado = list(map(cuadrado,a))
# resultado_lambda = list(map(lambda num: num**2, a))
# # print(resultado_lambda)

# def mapeo(given_list):
#     for value in given_list:
#         # lambda value: value **2
#         value ** 2

# resultado_filtro = list(filter(lambda num: num >2, a))

# num = 2

# print(num.__str__())

# def outter(inner_func):
#     def inner():
#         return inner_func
#     return inner()

# @outter
# def hola(msg):
#     return msg

# test = outter("hola")
# print(test)

diccionario = {"sumar": lambda a,b: a + b}
# print(diccionario["sumar"])

def contenedor(msg): # == @property
    def saludar(msg):
        return msg

    return saludar(msg)

test= contenedor("Otra cosa!")
print(test)



# a = iter([1,2,3,4])

# map(lambda num: num, a)
# # for i,values in enumerate(a):
# #     print(i, value)
# print(reduce(lambda num1,num2: num1 / num2, a))

# def reduce_en_casa(given):
#     num1 = next(given)
#     try:
#         for num2 in given:
#             num1+=num2
#     except:
#         return num1

# test = reduce_en_casa(a)
# print(test)