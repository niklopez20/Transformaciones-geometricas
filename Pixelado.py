from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def pixelar(imagen, tamaño_bloque):
    # Convertir la imagen a un array numpy
    array_imagen = np.array(imagen)
    altura, anchura, _ = array_imagen.shape

    # Crear un nuevo array para la imagen pixelada
    array_pixelada = np.zeros_like(array_imagen)

    # Recorrer la imagen en pasos del tamaño del bloque
    for y in range(0, altura, tamaño_bloque):
        for x in range(0, anchura, tamaño_bloque):
            # Definir la región para el bloque actual
            bloque = array_imagen[y:y + tamaño_bloque, x:x + tamaño_bloque]
            
            # Calcular el color promedio del bloque
            color_promedio = bloque.reshape(-1, 3).mean(axis=0)
            
            # Asignar el color promedio al bloque en el nuevo array
            array_pixelada[y:y + tamaño_bloque, x:x + tamaño_bloque] = color_promedio
    
    # Convertir el nuevo array de vuelta a una imagen PIL
    return Image.fromarray(array_pixelada.astype(np.uint8))


# Importar la imagen
ruta_imagen = 'C:/Users/luisl.LAPTOP-INSANA/Documents/IPN/Procesamiento de Imagenes/3er parcial/IMG_2955.JPEG'  # Reemplaza con la ruta a tu imagen
imagen = Image.open(ruta_imagen)

# Establecer el tamaño del bloque para el pixelado
tamaño_bloque = 10  # Tamaño del bloque para el efecto de pixelado

# Aplicar el efecto de pixelado a la imagen
imagen_pixelada = pixelar(imagen, tamaño_bloque)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(imagen)
axes[0].set_title('Imagen Original')
axes[0].axis('off')

axes[1].imshow(imagen_pixelada)
axes[1].set_title(f'Imagen Pixelada (Tamaño de Bloque={tamaño_bloque})')
axes[1].axis('off')

plt.show()
