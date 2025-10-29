# iter_4.py

class UppercaseIterator:
  """Iterador que devuelve elementos de una lista en mayúsculas."""
  def __init__(self, lista_cadenas):
    self._lista = lista_cadenas
    self._indice = 0 

  def __iter__(self):
    
    return self

  def __next__(self):
    if self._indice < len(self._lista):
      
      cadena_mayus = self._lista[self._indice].upper()
      self._indice += 1
      return cadena_mayus
    else:
      
      raise StopIteration

cadenas = ["manzana", "pera", "uva", "kiwi"]
iterador_mayus = UppercaseIterator(cadenas)

print("Cadenas en mayúsculas usando un iterador personalizado:")
for item in iterador_mayus:
  print(item)