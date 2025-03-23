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