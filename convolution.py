import numpy as np

# Funcion convolution que recibe como input la matriz y el kernel.
def convolution(matriz, kernel):
    
    row_matriz = len(matriz) # Cantidad de filas en la matriz.
    col_matriz = len(matriz[0]) # Cantidad de columnas en la matriz.
    row_kernel = len(kernel) # Cantidad de filas en el kernel.
    col_kernel = len(kernel[0]) # Cantidad de columnas en el kernel.

# Se verifica si la matriz es de menor tamaño que el kernel.
    if(col_matriz<col_kernel or row_matriz<row_kernel):
        return

# Calculo de dimension de matriz de output.
    row_salida = row_matriz - row_kernel + 1
    col_salida = col_matriz - col_kernel + 1
    salida = np.zeros((row_salida, col_salida))

# Recorido de la matriz y kernel.
    for i in range(row_salida):
        for j in range(col_salida):
            total = 0
            for row in range(row_kernel):
                for col in range(col_kernel):
                    total += matriz[i + row, j + col] * kernel[row, col]  # Calculo de convolución.
            salida[i, j] = total

    return salida


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