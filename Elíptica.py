import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def transformacion_eliptica(imagen, a, eje='x'):
    array_imagen = np.array(imagen)
    altura, anchura, _ = array_imagen.shape
    array_eliptica = np.zeros_like(array_imagen)

    if eje == 'x':
        for y in range(altura):
            for x in range(anchura):
                x_normalizado = 2 * (x / anchura) - 1  # Normalizar x al rango [-1, 1]
                factor = np.sqrt(max(0, 1 - (a * x_normalizado) ** 2))
                nuevo_x = int((factor * x_normalizado + 1) * anchura / 2)
                if 0 <= nuevo_x < anchura:
                    array_eliptica[y, nuevo_x] = array_imagen[y, x]
    elif eje == 'y':
        for y in range(altura):
            for x in range(anchura):
                y_normalizado = 2 * (y / altura) - 1  # Normalizar y al rango [-1, 1]
                factor = np.sqrt(max(0, 1 - (a * y_normalizado) ** 2))
                nuevo_y = int((factor * y_normalizado + 1) * altura / 2)
                if 0 <= nuevo_y < altura:
                    array_eliptica[nuevo_y, x] = array_imagen[y, x]

    return Image.fromarray(array_eliptica)

# Cargar la imagen
ruta_imagen = 'C:/Users/luisl.LAPTOP-INSANA/Documents/IPN/Procesamiento de Imagenes/3er parcial/IMG_2955.JPEG'
imagen = Image.open(ruta_imagen)

# Establecer el parámetro 'a' para la transformación elíptica
a = 0.75  # Valor específico de 'a'

# Aplicar la transformación elíptica
imagen_eliptica_x = transformacion_eliptica(imagen, a, eje='x')
imagen_eliptica_y = transformacion_eliptica(imagen, a, eje='y')

# Mostrar las imágenes original y elípticas
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
axes[0].imshow(imagen)
axes[0].set_title('Imagen de entrada')
axes[0].axis('off')

axes[1].imshow(imagen_eliptica_x)
axes[1].set_title(f'Tr. elíptica en X (a={a})')
axes[1].axis('off')

axes[2].imshow(imagen_eliptica_y)
axes[2].set_title(f'Tr. elíptica en Y (a={a})')
axes[2].axis('off')

plt.show()
