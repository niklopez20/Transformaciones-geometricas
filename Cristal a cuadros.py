from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import random

def efecto_cristal_cuadros(imagen, tamano_bloque):
    # Convertir la imagen a un array numpy
    array_imagen = np.array(imagen)
    altura, anchura, _ = array_imagen.shape

    # Crear un nuevo array para la imagen con efecto de cristal a cuadros
    array_cristal = np.zeros_like(array_imagen)

    # Recorrer la imagen en pasos del tamaño del bloque
    for y in range(0, altura, tamano_bloque):
        for x in range(0, anchura, tamano_bloque):
            # Seleccionar aleatoriamente un píxel dentro del bloque
            random_y = y + random.randint(0, tamano_bloque - 1)
            random_x = x + random.randint(0, tamano_bloque - 1)

            # Asegurarse de que las coordenadas aleatorias estén dentro de los límites de la imagen
            random_y = min(random_y, altura - 1)
            random_x = min(random_x, anchura - 1)

            # Obtener el color del píxel seleccionado aleatoriamente
            color_aleatorio = array_imagen[random_y, random_x]

            # Asignar el color aleatorio a todo el bloque en el nuevo array
            array_cristal[y:y + tamano_bloque, x:x + tamano_bloque] = color_aleatorio

    # Convertir el nuevo array de vuelta a una imagen PIL
    return Image.fromarray(array_cristal.astype(np.uint8))

# Cargar la imagen
ruta_imagen = 'C:/Users/luisl.LAPTOP-INSANA/Documents/IPN/Procesamiento de Imagenes/3er parcial/IMG_2955.JPEG'  # Reemplaza con la ruta a tu imagen
imagen = Image.open(ruta_imagen)

# Establecer el tamaño del bloque para el efecto de cristal a cuadros
tamano_bloque = 10  # Tamaño del bloque para el efecto de cristal a cuadros

# Aplicar el efecto de cristal a cuadros a la imagen
imagen_cristal = efecto_cristal_cuadros(imagen, tamano_bloque)

# Mostrar las imágenes original y con efecto de cristal a cuadros
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(imagen)
axes[0].set_title('Imagen Original')
axes[0].axis('off')

axes[1].imshow(imagen_cristal)
axes[1].set_title(f'Efecto de Cristal a Cuadros (Tamaño de Bloque={tamano_bloque})')
axes[1].axis('off')

plt.show()
