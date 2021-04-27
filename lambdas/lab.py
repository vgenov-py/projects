a = [1,2,3,4]

def cuadrados(given_list):
    result = []
    for num in given_list:
        result.append(num**2)
    return result

funcion = cuadrados
print(cuadrados)
print(funcion)
