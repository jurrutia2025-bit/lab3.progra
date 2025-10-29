from functools import reduce

lista_cadenas = ["Hola", " ", "Mundo", " ¡", "Python"]


cadena_final = reduce(lambda acc, x: acc + x, lista_cadenas)

print("Lista de cadenas:", lista_cadenas)
print("Cadena final:", cadena_final)