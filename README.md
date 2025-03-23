# Trabajos-Independientes-A01255262

### Autor: Kimberly Gabriela Marquez Preciado

## Descripción
Este repositorio contiene tres funciones principales relacionadas con el procesamiento de imágenes. Estas funciones fueron implementadas como parte de los conocimientos adquiridos en clase. Las funciones implementadas son:

1. **Convolution**: Esta función aplica un filtro a una matriz utilizando un kernel específico. Se utiliza en la operación de convolución, que es fundamental en el procesamiento de imágenes.
2. **Convolutionimg**: Función adaptada para trabajar con imágenes en formato 3D (RGB). Realiza la convolución de la imagen utilizando el kernel especificado.
3. **Padding**: Esta función agrega un borde de ceros alrededor de una imagen o matriz. 

## Funciones
### `convolution(matriz, kernel)`
Esta función aplica una convolución a una matriz utilizando un kernel específico. Recibe como parámetros una matriz (imagen o arreglo 2D) y un kernel (también 2D). El resultado es una nueva matriz que representa el resultado de la operación de convolución.

- **Entradas:**
  - `matriz`: Una matriz 2D que representa la imagen o datos a procesar.
  - `kernel`: Un kernel 2D utilizado para realizar la convolución.
  
- **Salidas:**
  - `salida`: La matriz resultante después de aplicar la convolución.

### `convolutionimg(matriz, kernel)`
Esta función realiza una convolución adaptada para imágenes. La diferencia con `convolution` es que esta operación es aplicada en imágenes con múltiples canales (por ejemplo, RGB). Cada canal de la imagen se procesa por separado.

- **Entradas:**
  - `matriz`: Una imagen en formato 3D (filas x columnas x canales).
  - `kernel`: Un kernel 2D para realizar la convolución en la imagen.
  
- **Salidas:**
  - `salida`: La imagen resultante después de aplicar la convolución, con el tamaño ajustado y los valores de píxeles normalizados.

### `padding(matriz, padding)`
La función `padding` agrega un borde de ceros alrededor de una imagen o matriz. Se utiliza para asegurar que al aplicar convoluciones a los bordes de la imagen, no se pierdan detalles importantes.

- **Entradas:**
  - `matriz`: Una matriz (o imagen) a la que se le aplicará padding.
  - `padding`: La cantidad de ceros a agregar alrededor de la imagen.
  
- **Salidas:**
  - `salida`: La matriz con el padding agregado.

## Ejemplo de Uso

### Estos se pueden encontrar en el archivo main.py

