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

a = [1,2,3,4]
b = map(lambda num: num, a)
for num in b:
    print(num)


def cuadrado(num):
    return num ** 2
resultado = list(map(cuadrado,a))
resultado_lambda = list(map(lambda num: num**2, a))
# print(resultado_lambda)

def mapeo(given_list):
    for value in given_list:
        # lambda value: value **2
        value ** 2

resultado_filtro = list(filter(lambda num: num >2, a))



