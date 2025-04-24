import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def transformacion_abombada(imagen, fuerza):
    array_imagen = np.array(imagen)
    altura, anchura, _ = array_imagen.shape
    centro_x, centro_y = anchura / 2, altura / 2
    radio_maximo = np.sqrt(centro_x**2 + centro_y**2)
    
    def abombar(x, y):
        dx, dy = x - centro_x, y - centro_y
        distancia = np.sqrt(dx**2 + dy**2)
        if distancia == 0:
            return x, y
        distancia_abombada = (distancia / radio_maximo) ** fuerza * radio_maximo
        proporcion = distancia_abombada / distancia
        return centro_x + dx * proporcion, centro_y + dy * proporcion

    array_abombado = np.zeros_like(array_imagen)
    
    for y in range(altura):
        for x in range(anchura):
            nuevo_x, nuevo_y = abombar(x, y)
            nuevo_x, nuevo_y = int(nuevo_x), int(nuevo_y)
            if 0 <= nuevo_x < anchura and 0 <= nuevo_y < altura:
                array_abombado[y, x] = array_imagen[nuevo_y, nuevo_x]

    return Image.fromarray(array_abombado)

# Cargar la imagen
ruta_imagen = 'C:/Users/luisl.LAPTOP-INSANA/Documents/IPN/Procesamiento de Imagenes/3er parcial/xd.jpg'
imagen = Image.open(ruta_imagen)

# Establecer la fuerza para el efecto abombado
fuerza = 1.5  # Puedes ajustar este valor para ver diferentes efectos

# Aplicar la transformación abombada
imagen_abombada = transformacion_abombada(imagen, fuerza)

# Mostrar las imágenes original y abombada
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(imagen)
axes[0].set_title('Imagen de entrada')
axes[0].axis('off')

axes[1].imshow(imagen_abombada)
axes[1].set_title(f'Efecto Abombado (fuerza={fuerza})')
axes[1].axis('off')

plt.show()
