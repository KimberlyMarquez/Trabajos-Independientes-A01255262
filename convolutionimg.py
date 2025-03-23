import numpy as np

# Es la logica de la funcion convolution pero con adaptaciones para imagenes.

def convolutionimg(matriz, kernel):
    row_matriz, col_matriz, canales_matriz = matriz.shape
    row_kernel, col_kernel = kernel.shape

    if col_matriz < col_kernel or row_matriz < row_kernel:
        return None

    # Calcular el tamaño de la salida
    row_salida = row_matriz - row_kernel + 1
    col_salida = col_matriz - col_kernel + 1
    salida = np.zeros((row_salida, col_salida, canales_matriz))

    for i in range(row_salida):
        for j in range(col_salida):
            # Calcular el valor de la convolución para cada canal
            for k in range(canales_matriz):
                total = 0
                for row in range(row_kernel):
                    for col in range(col_kernel):
                        total += matriz[i + row, j + col, k] * kernel[row, col]
                salida[i, j, k] = total

    salida = np.clip(salida, 0, 255).astype(np.uint8)  # Normalizar la salida
    return salida
