import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def transformacion_ondulacion(imagen, frecuencia=10, amplitud=5):
    array_imagen = np.array(imagen)
    altura, anchura, _ = array_imagen.shape
    centro_x, centro_y = anchura / 2, altura / 2

    def ondulacion(x, y):
        dx, dy = x - centro_x, y - centro_y
        distancia = np.sqrt(dx**2 + dy**2)
        angulo = np.arctan2(dy, dx)
        efecto_ondulacion = amplitud * np.sin(frecuencia * distancia / max(anchura, altura) * 2 * np.pi)
        nuevo_x = int(centro_x + (distancia + efecto_ondulacion) * np.cos(angulo))
        nuevo_y = int(centro_y + (distancia + efecto_ondulacion) * np.sin(angulo))
        return nuevo_x, nuevo_y

    array_ondulado = np.zeros_like(array_imagen)

    for y in range(altura):
        for x in range(anchura):
            nuevo_x, nuevo_y = ondulacion(x, y)
            if 0 <= nuevo_x < anchura and 0 <= nuevo_y < altura:
                array_ondulado[y, x] = array_imagen[nuevo_y, nuevo_x]

    return Image.fromarray(array_ondulado)

# Cargar la imagen
ruta_imagen = 'C:/Users/luisl.LAPTOP-INSANA/Documents/IPN/Procesamiento de Imagenes/3er parcial/IMG_2955.JPEG'
imagen = Image.open(ruta_imagen)

# Establecer la frecuencia y amplitud para el efecto de ondulación
frecuencia = 20  # Puedes ajustar este valor para ver diferentes efectos
amplitud = 15  # Puedes ajustar este valor para ver diferentes efectos

# Aplicar la transformación de ondulación
imagen_ondulada = transformacion_ondulacion(imagen, frecuencia, amplitud)

# Mostrar las imágenes original y ondulada
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(imagen)
axes[0].set_title('Imagen de entrada')
axes[0].axis('off')

axes[1].imshow(imagen_ondulada)
axes[1].set_title(f'Efecto de Ondulación (frecuencia={frecuencia}, amplitud={amplitud})')
axes[1].axis('off')

plt.show()
