import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
from scipy.ndimage import map_coordinates

def S(x, y, sigma):
    return np.exp(-((x)**2 + (y)**2) / sigma**2)

def pinch_transform(image, sigma, a):
    rows, cols = image.shape[:2]
    y, x = np.meshgrid(np.arange(rows), np.arange(cols), indexing='ij')

    # Centro de la imagen
    cx, cy = cols // 2, rows // 2

    # Calcula la distancia al centro de deformación
    dx = x - cx
    dy = y - cy
    distance_squared = dx**2 + dy**2

    # Calcula el factor de transformación
    S_xy = S(dx, dy, sigma)

    # Modificar la distancia radial basada en el parámetro de fuerza
    distance = np.sqrt(distance_squared)
    distance_new = distance / (1 + a * S_xy)  # Ajustar para que a < 0 estire y a > 0 comprima

    # Calcular las nuevas coordenadas
    x_new = cx + (dx / (distance + 1e-6)) * distance_new
    y_new = cy + (dy / (distance + 1e-6)) * distance_new

    # Interpola la imagen original en las nuevas coordenadas
    transformed_image = np.zeros_like(image)
    for i in range(3):  # Para cada canal de color
        transformed_image[..., i] = map_coordinates(image[..., i], [y_new, x_new], order=1, mode='reflect')
 
    return transformed_image, x, y

# Cargar la imagen y reducir su resolución
image_path = 'C:/Users/luisl.LAPTOP-INSANA/Documents/IPN/Procesamiento de Imagenes/3er parcial/xd.jpg'  # Reemplaza con la ruta a tu imagen
image = Image.open(image_path)
image = image.resize((300, 300))  # Redimensionar para reducir la carga computacional
image = np.array(image)

# Parámetros de la transformación
sigma = 3  # Anchura de la zona deformada
a = 5  # Fuerza de la deformación (comprimir)

# Aplicar la transformación
transformed_image, x, y = pinch_transform(image, sigma, a)

# Crear el gráfico 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Superficie 3D con la imagen deformada
ax.plot_surface(x, y, np.ones_like(x), rstride=1, cstride=1, facecolors=transformed_image / 255.0, shade=False)

# Ajustar la vista y etiquetas
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Deformación')
ax.set_title(f'Superficie de la Imagen Deformada ($\sigma$={sigma}, a={a})')

plt.show()
