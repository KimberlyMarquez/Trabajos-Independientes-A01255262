import numpy as np
import matplotlib.pyplot as plt
import cv2
from convolution import convolution
from convolutionimg import convolutionimg
from padding import padding

print("\nFunción Convolution con Matriz")

# Caso de Prueba 1
print("\nCaso de Prueba 1")

matriz1 = np.array([
    [3, 0, 1, 2, 7],
    [1, 5, 8, 9, 3],
    [2, 7, 2, 5, 1],
    [0, 1, 3, 1, 7],
    [4, 2, 1, 6, 2]])

kernel1 = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]])

resultado1 = convolution(matriz1, kernel1)
print(resultado1)

# Caso de Prueba 2
print("\nCaso de Prueba 2")

matriz2 = np.array([
    [3, 0, 1],
    [1, 5, 8],
    [2, 7, 2]])

kernel2 = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]])

resultado2 = convolution(matriz2, kernel2)
print(resultado2)

# Caso de Prueba 3
print("\nCaso de Prueba 3")

matriz3 = np.array([
    [1, 2],
    [3, 4]])

kernel3 = np.array([
    [1, 0, -1],
    [1, 0, -1],
    [1, 0, -1]])

resultado3 = convolution(matriz3, kernel3)
print(resultado3)

# NOTA: En este caso aparecera un NONE. Puesto que la matriz es menor que el kernel.

# Caso de Prueba 4
print("\nCaso de Prueba 4")
matriz4 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])

kernel4 = np.array([
    [1, 0],
    [0, -1]])

resultado4 = convolution(matriz4, kernel4)
print(resultado4)
print("\n")

print("------------------------------------------------------------")
print("\nPrueba de funciones padding y convolutionimg con imagen.")

kernel_emboss = np.array([
    [-2, -1, 0],
    [-1, 1, 1],
    [0, 1, 2]
])

ruta = "img/img1.jpg"

img = cv2.imread(ruta, cv2.IMREAD_COLOR_RGB)
img = convolutionimg(img, kernel_emboss)
img = padding(img, 1)
plt.imshow(img)
plt.axis('off')
plt.show()
