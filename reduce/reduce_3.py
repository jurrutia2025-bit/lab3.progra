from functools import reduce

lista_max = [7, 3, 9, 1, 5, 12, 4]


mayor_num = reduce(lambda acc, x: acc if acc > x else x, lista_max)

print("Lista de números:", lista_max)
print("Número mayor:", mayor_num)