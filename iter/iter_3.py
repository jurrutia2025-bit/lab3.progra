class CuadradosLista:
  """Clase que devuelve la lista completa de cuadrados sin usar iteradores."""
  def obtener_cuadrados(self):
    
    lista_completa = [i * i for i in range(1, 11)]
    return lista_completa

clase_lista = CuadradosLista()
print("Lista completa de cuadrados (método simple):")
print(clase_lista.obtener_cuadrados())