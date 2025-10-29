class CuadradosGenerador:
  """Clase que usa yield en __iter__ para generar los cuadrados del 1 al 10."""
  def __iter__(self):
   
    for i in range(1, 11):
      yield i * i

print("Cuadrados del 1 al 10 (Generador en Clase):")
for cuadrado in CuadradosGenerador():
  print(cuadrado)