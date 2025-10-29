from functools import reduce

lista_mult = [2, 3, 4]


total_mult = reduce(lambda acc, x: acc * x, lista_mult)

print("Lista a multiplicar:", lista_mult)
print("Multiplicación total:", total_mult)