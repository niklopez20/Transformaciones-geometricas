import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.ndimage import map_coordinates

def pinch_effect(image, cx, cy, sigma, a):
    """
    Aplica el efecto de pinchar/estirar a una imagen utilizando la fórmula proporcionada con el parámetro de fuerza.

    Parámetros:
    image (ndarray): Imagen de entrada en formato numpy array.
    cx, cy (int): Coordenadas del centro de la deformación.
    sigma (float): Anchura de la zona deformada.
    a (float): Fuerza de la deformación; a < 0 para estirar, a > 0 para comprimir.
    
    Retorna:
    ndarray: Imagen transformada.
    """
    rows, cols = image.shape[:2]
    y, x = np.meshgrid(np.arange(rows), np.arange(cols), indexing='ij')

    # Calcula la distancia al centro de deformación
    dx = x - cx
    dy = y - cy
    distance_squared = dx**2 + dy**2

    # Calcula el factor de transformación
    S = np.exp(-distance_squared / sigma**2)

    # Modificar la distancia radial basada en el parámetro de fuerza
    distance = np.sqrt(distance_squared)
    distance_new = distance / (1 + a * S)  # Ajustar para que a < 0 estire y a > 0 comprima

    # Calcular las nuevas coordenadas
    x_new = cx + (dx / (distance + 1e-6)) * distance_new
    y_new = cy + (dy / (distance + 1e-6)) * distance_new

    # Interpola la imagen original en las nuevas coordenadas
    transformed_image = np.zeros_like(image)
    for i in range(3):  # Para cada canal de color
        transformed_image[..., i] = map_coordinates(image[..., i], [y_new, x_new], order=1, mode='reflect')
    
    return transformed_image

# Cargar una imagen de ejemplo
image_path = 'C:/Users/luisl.LAPTOP-INSANA/Documents/IPN/Procesamiento de Imagenes/3er parcial/perro3.jpg'  # Reemplaza con la ruta a tu imagen
image = Image.open(image_path)
image = np.array(image)

# Parámetros de la transformación
cx, cy = image.shape[1] // 2, image.shape[0] // 2  # Centro de la imagen
sigma = 100  # Anchura de la zona deformada
a = -.8  # Fuerza de la deformación (comprimir)

# Aplicar la transformación
transformed_image = pinch_effect(image, cx, cy, sigma, a)

# Mostrar la imagen original y la transformada
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title('Imagen Original')
plt.imshow(image)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Imagen con Efecto Pinchar/Estirar')
plt.imshow(transformed_image)
plt.axis('off')

plt.show()
