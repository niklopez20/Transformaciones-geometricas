from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def efecto_pinchar(imagen, fuerza=0.5):
    # Convertir la imagen a un arreglo de numpy
    array_imagen = np.array(imagen)
    altura, anchura, _ = array_imagen.shape

    # Crear la cuadrícula de coordenadas
    x, y = np.meshgrid(np.linspace(-1, 1, anchura), np.linspace(-1, 1, altura))
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)

    # Aplicar el efecto a todas las coordenadas
    r_pinchar = r**fuerza
    x_nuevo = r_pinchar * np.cos(theta)
    y_nuevo = r_pinchar * np.sin(theta)

    # Reasignar las coordenadas
    x_nuevo = ((x_nuevo + 1) * (anchura - 1) / 2).astype(int)
    y_nuevo = ((y_nuevo + 1) * (altura - 1) / 2).astype(int)

    # Asegurar que las nuevas coordenadas estén dentro de los límites
    x_nuevo = np.clip(x_nuevo, 0, anchura - 1)
    y_nuevo = np.clip(y_nuevo, 0, altura - 1)

    # Crear un nuevo arreglo con las coordenadas transformadas
    array_imagen_nueva = array_imagen[y_nuevo, x_nuevo]

    # Convertir el nuevo arreglo de vuelta a una imagen PIL
    return Image.fromarray(array_imagen_nueva)

ruta_imagen = 'C:/Users/luisl.LAPTOP-INSANA/Documents/IPN/Procesamiento de Imagenes/3er parcial/IMG_2955.JPEG'  # Reemplaza con la ruta a tu imagen
imagen = Image.open(ruta_imagen)

imagen_pinchar = efecto_pinchar(imagen,)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(imagen)
axes[0].set_title('Imagen Original')
axes[0].axis('off')

axes[1].imshow(imagen_pinchar)
axes[1].set_title('Imagen con Efecto Pinchar')
axes[1].axis('off')

plt.show()
