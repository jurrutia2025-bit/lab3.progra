animales = ["perro", "gato", "pato", "hamster", "pez"]

con_p = list(filter(lambda x: x.startswith('p'), animales))

print("Lista de animales:", animales)
print("Palabras que empiezan con 'p':", con_p)