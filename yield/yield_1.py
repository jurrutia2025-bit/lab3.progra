def generar_pares():
  """Genera los primeros 10 números pares usando yield."""
  contados = 0
  numero = 0
  while contados < 10:
    if numero % 2 == 0:
      yield numero
      contados += 1
    numero += 1


print("Primeros 10 números pares:")
for par in generar_pares():
  print(par)