import requests as req
from functools import reduce
import time
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
# start = time.perf_counter()
# diccionario = {"sumar": lambda a,b: a + b}
# # print(diccionario["sumar"])

# def contenedor(msg): # == @property
#     def saludar(msg):
#         return msg

#     return saludar(msg)

# test= contenedor("Otra cosa!")
# print(test)



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

# ERROR HANDLING:

# a = 1
# b = 2
# if True:
#     print("hola")

# try: 
#     print(a+b)
# except: 
#     print("No son números")
# finish = time.perf_counter()
# print(finish-start)

a = [1,2,3,4]
#[num for num in a]
#[num for num in a if num %2 == 0]
#[num *2 if num %2 == 0 else num for num in a]


#OPERADORES TERNARIOS
a = [1,2,3,4]

#NÚMEROS PARES CON TERNARIO Y COMPREHENSION:
result_ternario = [num*2 if num %2 == 0 else num for num in a ]
result = list(map(lambda num: num*2 if num %2 ==0 else num,a))
# print(result_ternario)

age = 15
is_adult = 20 if age >= 18 else "string"
# print(is_adult)
# is_adult = None
# if age>= 18:
#     print(True)
# else:
#     print(False)


# a = [1,2,3,4]
# def doble(num):
#     return num ** 2
# listado = [doble(num) for num in a]




# #con comprehension
# result_en_lista = sum([num ** 2 for num in a])

# #con generator sintaxis comprehension
# result_en_generador = (num ** 2 for num in a)
# # print(result_en_lista)
# # print(type(result_1))


# # con función normal
# def dobles(given_list):
#     result = []
#     for num in given_list:
#         result.append(num ** 2)
#     return result

# #con función generadora
# def dobles_generator(given_list):
#     for num in given_list:
#         yield num ** 2

# result_2 = dobles(a)


# # con la función de Ricardo:
# result_map = map(lambda num: num ** 2, a)


# a = [1,2,3,4]

# result = [num ** 2 for num in a]
# result = [num** 2 for  num in a  if num%2==0]
# result = [num** 2 if num%2==0 else num for num in a]

# print(result)

def unafuncion():
    return "menu"

a = [1,2,3,4]
num = 12

result = "Es 100" if num == 100 else "Es 10"


# if num == 100:
#     print("Es 100")
# else:
#     if num == 10:
#         print("Es 10")
#     else:
#         if num == 1:
#             print("Es 1")
#         else:
#             print("No es ninguno de los tres números mágicos")


a = [1,2,3,4]
b = [num  for num  in a]

result = list(map(lambda num: num if num %2 == 0 else None,a))
result_comprehension = [num for num in a if num %2 == 0]
print(result_comprehension)