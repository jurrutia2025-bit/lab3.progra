def generar_impares(lista_numeros):
  """Genera solo los números impares de una lista usando yield."""
  for num in lista_numeros:
    if num % 2 != 0:
      yield num

numeros = [1, 4, 7, 10, 13, 16, 19, 22]

print("Números impares de la lista:")
for impar in generar_impares(numeros):
  print(impar)