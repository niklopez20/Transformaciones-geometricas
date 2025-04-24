import cv2
import numpy as np
import matplotlib.pyplot as plt

def transformacion_cilindrica(img, longitud_focal, eje='x'):
    h, w = img.shape[:2]
    
    # Inicializar la imagen de salida
    img_cilindrica = np.zeros_like(img)

    if eje == 'x':
        for y in range(h):
            for x in range(w):
                theta = (x - w / 2) / longitud_focal
                h_ = (y - h / 2) / longitud_focal

                X = np.sin(theta)
                Y = h_
                Z = np.cos(theta)

                x_ = longitud_focal * X / Z + w / 2
                y_ = longitud_focal * Y / Z + h / 2

                if 0 <= x_ < w and 0 <= y_ < h:
                    x0 = int(np.floor(x_))
                    x1 = min(x0 + 1, w - 1)
                    y0 = int(np.floor(y_))
                    y1 = min(y0 + 1, h - 1)
                    dx = x_ - x0
                    dy = y_ - y0
                    img_cilindrica[y, x] = (img[y0, x0] * (1 - dx) * (1 - dy) +
                                            img[y1, x0] * (1 - dx) * dy +
                                            img[y0, x1] * dx * (1 - dy) +
                                            img[y1, x1] * dx * dy)
    elif eje == 'y':
        for y in range(h):
            for x in range(w):
                theta = (y - h / 2) / longitud_focal
                w_ = (x - w / 2) / longitud_focal

                Y = np.sin(theta)
                X = w_
                Z = np.cos(theta)

                y_ = longitud_focal * Y / Z + h / 2
                x_ = longitud_focal * X / Z + w / 2

                if 0 <= x_ < w and 0 <= y_ < h:
                    x0 = int(np.floor(x_))
                    x1 = min(x0 + 1, w - 1)
                    y0 = int(np.floor(y_))
                    y1 = min(y0 + 1, h - 1)
                    dx = x_ - x0
                    dy = y_ - y0
                    img_cilindrica[y, x] = (img[y0, x0] * (1 - dx) * (1 - dy) +
                                            img[y1, x0] * (1 - dx) * dy +
                                            img[y0, x1] * dx * (1 - dy) +
                                            img[y1, x1] * dx * dy)

    return img_cilindrica

# Cargar la imagen
img = cv2.imread('C:/Users/luisl.LAPTOP-INSANA/Documents/IPN/Procesamiento de Imagenes/3er parcial/IMG_2955.JPEG')

# Definir la longitud focal (ajusta este valor según sea necesario)
longitud_focal = 300  # Ajustar este valor para obtener una mejor transformación

# Aplicar la transformación cilíndrica en el eje X
imagen_cilindrica_x = transformacion_cilindrica(img, longitud_focal, eje='x')

# Aplicar la transformación cilíndrica en el eje Y
imagen_cilindrica_y = transformacion_cilindrica(img, longitud_focal, eje='y')

# Crear la figura y los ejes
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Mostrar la imagen original
axes[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axes[0].set_title('Imagen Original')
axes[0].axis('off')

# Mostrar la imagen transformada en el eje X
axes[1].imshow(cv2.cvtColor(imagen_cilindrica_x, cv2.COLOR_BGR2RGB))
axes[1].set_title('Proyección Cilíndrica en X')
axes[1].axis('off')

# Mostrar la imagen transformada en el eje Y
axes[2].imshow(cv2.cvtColor(imagen_cilindrica_y, cv2.COLOR_BGR2RGB))
axes[2].set_title('Proyección Cilíndrica en Y')
axes[2].axis('off')

# Mostrar la figura
plt.show()