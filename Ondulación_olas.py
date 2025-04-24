from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def efecto_onda(imagen, amplitud=5, frecuencia=20):
    # Convertir la imagen a un arreglo de numpy
    array_imagen = np.array(imagen)
    altura, anchura, _ = array_imagen.shape

    # Crear la cuadrícula de coordenadas
    x, y = np.meshgrid(np.arange(anchura), np.arange(altura))
    
    # Aplicar la transformación de onda
    x_onda = x + amplitud * np.sin(2 * np.pi * y / frecuencia)
    y_onda = y + amplitud * np.sin(2 * np.pi * x / frecuencia)

    # Mapear las nuevas coordenadas de vuelta a las coordenadas de la imagen
    x_onda = np.clip(x_onda, 0, anchura - 1).astype(int)
    y_onda = np.clip(y_onda, 0, altura - 1).astype(int)

    # Crear un nuevo arreglo de imagen con las coordenadas transformadas
    array_imagen_nueva = array_imagen[y_onda, x_onda]

    # Convertir el arreglo de numpy de vuelta a una imagen PIL
    return Image.fromarray(array_imagen_nueva)

# Cargar la imagen
ruta_imagen = 'C:/Users/luisl.LAPTOP-INSANA/Documents/IPN/Procesamiento de Imagenes/3er parcial/IMG_2955.JPEG'  # Reemplaza con la ruta a tu imagen
imagen = Image.open(ruta_imagen)

# Ajustar la amplitud y la frecuencia del efecto de onda
amplitud = 5  # Amplitud de la ondulación
frecuencia = 15  # Frecuencia de la ondulación

# Aplicar el efecto de onda a la imagen
imagen_onda = efecto_onda(imagen, amplitud=amplitud, frecuencia=frecuencia)

# Mostrar las imágenes original y con efecto de onda
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(imagen)
axes[0].set_title('Imagen Original')
axes[0].axis('off')

axes[1].imshow(imagen_onda)
axes[1].set_title(f'Imagen con Efecto de Onda (Amplitud={amplitud}, Frecuencia={frecuencia})')
axes[1].axis('off')

plt.show()
