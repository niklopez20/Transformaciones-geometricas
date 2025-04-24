from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image_path = 'C:/Users/luisl.LAPTOP-INSANA/Documents/IPN/Procesamiento de Imagenes/3er parcial/IMG_2955.JPEG'  
image = Image.open(image_path)

def pinch_effect(image, strength=0.5):
   #Convertir la imagen a un arreglo de numpy
    img_array = np.array(image)
    height, width, _ = img_array.shape

    #Crear la cuadricula de coordenadas
    x, y = np.meshgrid(np.linspace(-1, 1, width), np.linspace(-1, 1, height))
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)

    #Se aplica el efecto a todas las coordenadas
    r_pinch = r**strength
    x_new = r_pinch * np.cos(theta)
    y_new = r_pinch * np.sin(theta)

    #Se reasignan las coordenadas
    x_new = ((x_new + 1) * (width - 1) / 2).astype(int)
    y_new = ((y_new + 1) * (height - 1) / 2).astype(int)

    #Se aegura que las nuevas coordenadas están dentro de loos límites
    x_new = np.clip(x_new, 0, width - 1)
    y_new = np.clip(y_new, 0, height - 1)

    #Se crea un nuevo arreglo con las coordenadas tranformadas
    img_array_new = img_array[y_new, x_new]

    #Se convierte la imagen a un arreglo de numpy
    return Image.fromarray(img_array_new)

pinched_image = pinch_effect(image)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(image)
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(pinched_image)
axes[1].set_title('Image with Pinch Effect')
axes[1].axis('off')

plt.show()

def seleccionar_efecto ():
    print("Seleccione el efecto que desea aplicasr a la imagen:")
    print("1. Efecto Pinchar")
    print("2. Efecto Ondulación")
    eleccion= input("Ingrese el número correspondiente al efecto que se desea ejecutar: ")
    return eleccion

elecciondelalgoritmo = seleccionar_efecto()

if elecciondelalgoritmo == '1':
    algoritmo = pinch_effect
elif elecciondelalgoritmo == '2':
    algoritmo = 