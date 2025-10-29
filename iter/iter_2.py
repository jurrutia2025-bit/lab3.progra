class ImparesGenerador:
  """Clase que usa yield para generar impares e iterada con for."""
  def __iter__(self):
    for num in range(1, 21):
      if num % 2 != 0:
        yield num

print("Impares del 1 al 20 (Clase Generadora, iterado con for):")
for impar in ImparesGenerador():
  print(impar)