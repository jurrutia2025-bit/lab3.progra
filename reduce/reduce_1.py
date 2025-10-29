from functools import reduce

lista_suma = [5, 10, 15, 20]


total_suma = reduce(lambda acc, x: acc + x, lista_suma)

print("Lista a sumar:", lista_suma)
print("Suma total:", total_suma)