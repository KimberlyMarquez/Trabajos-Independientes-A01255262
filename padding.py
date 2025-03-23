import numpy as np

# Inputs de la funcion padding es la matriz y el padding a agregar.

def padding(matriz, padding):
  row, col, canales = matriz.shape  # Dimensiones de la matriz
  # Crea el output con el padding de ceros.
  salida = np.zeros((row+padding*2, col+padding*2, canales), dtype= matriz.dtype)
  salida[padding: padding + row, padding:padding + col, :] = matriz

  return salida
