lista_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

impares = list(filter(lambda x: x % 2 != 0, lista_nums))

print("Lista original:", lista_nums)
print("Números impares:", impares)