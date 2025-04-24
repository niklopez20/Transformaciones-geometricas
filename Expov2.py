from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import random

# Importar la imagen
ruta_imagen = 'C:/Users/luisl.LAPTOP-INSANA/Documents/IPN/Procesamiento de Imagenes/3er parcial/Expo/perro3.jpg'
imagen = Image.open(ruta_imagen)

# Función para pixelar la imagen
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

# Función para aplicar el efecto de cristal a cuadros
def efecto_cristal_cuadros(imagen, tamaño_bloque):
    # Convertir la imagen a un array numpy
    array_imagen = np.array(imagen)
    altura, anchura, _ = array_imagen.shape

    # Crear un nuevo array para la imagen con efecto de cristal a cuadros
    array_cristal = np.zeros_like(array_imagen)

    # Recorrer la imagen en pasos del tamaño del bloque
    for y in range(0, altura, tamaño_bloque):
        for x in range(0, anchura, tamaño_bloque):
            # Seleccionar aleatoriamente un píxel dentro del bloque
            random_y = y + random.randint(0, tamaño_bloque - 1)
            random_x = x + random.randint(0, tamaño_bloque - 1)

            # Asegurarse de que las coordenadas aleatorias estén dentro de los límites de la imagen
            random_y = min(random_y, altura - 1)
            random_x = min(random_x, anchura - 1)

            # Obtener el color del píxel seleccionado aleatoriamente
            color_aleatorio = array_imagen[random_y, random_x]

            # Asignar el color aleatorio a todo el bloque en el nuevo array
            array_cristal[y:y + tamaño_bloque, x:x + tamaño_bloque] = color_aleatorio

    # Convertir el nuevo array de vuelta a una imagen PIL
    return Image.fromarray(array_cristal.astype(np.uint8))

# Función para aplicar la transformación cilíndrica
def transformacion_cilindrica(imagen, longitud_focal, eje='x'):
    array_imagen = np.array(imagen)
    h, w = array_imagen.shape[:2]
    
    # Inicializar la imagen de salida
    img_cilindrica = np.zeros_like(array_imagen)

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
                    img_cilindrica[y, x] = (array_imagen[y0, x0] * (1 - dx) * (1 - dy) +
                                            array_imagen[y1, x0] * (1 - dx) * dy +
                                            array_imagen[y0, x1] * dx * (1 - dy) +
                                            array_imagen[y1, x1] * dx * dy)
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
                    img_cilindrica[y, x] = (array_imagen[y0, x0] * (1 - dx) * (1 - dy) +
                                            array_imagen[y1, x0] * (1 - dx) * dy +
                                            array_imagen[y0, x1] * dx * (1 - dy) +
                                            array_imagen[y1, x1] * dx * dy)

    return Image.fromarray(img_cilindrica.astype(np.uint8))

#Transformación elíptica
def transformacion_eliptica(imagen, a, eje='x'):
    array_imagen = np.array(imagen)
    altura, anchura, _ = array_imagen.shape
    array_eliptica = np.zeros_like(array_imagen)

    if eje == 'x':
        for y in range(altura):
            for x in range(anchura):
                x_normalizado = 2 * (x / anchura) - 1  # Normalizar x al rango [-1, 1]
                factor = np.sqrt(max(0, 1 - (a * x_normalizado) ** 2))
                nuevo_x = int((factor * x_normalizado + 1) * anchura / 2)
                if 0 <= nuevo_x < anchura:
                    array_eliptica[y, nuevo_x] = array_imagen[y, x]
    elif eje == 'y':
        for y in range(altura):
            for x in range(anchura):
                y_normalizado = 2 * (y / altura) - 1  # Normalizar y al rango [-1, 1]
                factor = np.sqrt(max(0, 1 - (a * y_normalizado) ** 2))
                nuevo_y = int((factor * y_normalizado + 1) * altura / 2)
                if 0 <= nuevo_y < altura:
                    array_eliptica[nuevo_y, x] = array_imagen[y, x]

    return Image.fromarray(array_eliptica)

#Transformación estirada (abombado)
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

#Transformación Ondulado
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

#Efecto Pinchar
def efecto_pinchar(imagen, fuerza = 0.5):
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

#Efeto ondas
def efecto_onda(imagen, amplitud, frecuencia):
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


# Aplicar los efectos a la imagen
tamaño_bloque = 10  #Pixelar y Cristal a cuadros
longitud_focal = 300    #Cilindrica
a = 0.75    #Eliptica
fuerza = 1.5 #Abombado
frecuencia = 20  # Ondulación y Olas
amplitud = 15    # Ondulación y Olas

imagen_pixelada = pixelar(imagen, tamaño_bloque)
imagen_cristal = efecto_cristal_cuadros(imagen, tamaño_bloque)
imagen_cilindrica_x = transformacion_cilindrica(imagen, longitud_focal, eje='x')
imagen_cilindrica_y = transformacion_cilindrica(imagen, longitud_focal, eje='y')
imagen_eliptica_x = transformacion_eliptica(imagen, a, eje='x')
imagen_eliptica_y = transformacion_eliptica(imagen, a, eje='y')
imagen_abombada = transformacion_abombada(imagen, fuerza)
imagen_ondulada = transformacion_ondulacion(imagen, frecuencia, amplitud)
imagen_pinchar = efecto_pinchar(imagen)
imagen_onda = efecto_onda(imagen, amplitud=amplitud, frecuencia=frecuencia)
fig, axes = plt.subplots(3, 4, figsize=(12, 6))
axes[0, 0].imshow(imagen)
axes[0, 0].set_title('Imagen Original')
axes[0, 0].axis('off')

axes[0, 1].imshow(imagen_pixelada)
axes[0, 1].set_title('Imagen Pixelada')
axes[0, 1].axis('off')

axes[0, 2].imshow(imagen_cristal)
axes[0, 2].set_title('Imagen Cristal a cuadros')
axes[0, 2].axis('off')

axes[0, 3].imshow(imagen_abombada)
axes[0, 3].set_title('Imagen Abombada')
axes[0, 3].axis('off')

axes[1, 0].imshow(imagen_cilindrica_x)
axes[1, 0].set_title('Transformación Cilíndrica X')
axes[1, 0].axis('off')
axes[1, 1].imshow(imagen_cilindrica_y)
axes[1, 1].set_title('Transformación Cilíndrica Y')
axes[1, 1].axis('off')

axes[1, 2].imshow(imagen_eliptica_x)
axes[1, 2].set_title('Transformación Elíptica X')
axes[1, 2].axis('off')
axes[1, 3].imshow(imagen_eliptica_y)
axes[1, 3].set_title('Transformación Elíptica Y')
axes[1, 3].axis('off')

axes[2,0].imshow(imagen_ondulada)
axes[2,0].set_title(f'Efecto de Ondulación (frecuencia={frecuencia}, amplitud={amplitud})')
axes[2,0].axis('off')

axes[2,1].imshow(imagen_pinchar)
axes[2,1].set_title('Efecto de Pinchar')
axes[2,1].axis('off')

axes[2,2].imshow(imagen_onda)
axes[2,2].set_title('Efecto de Ola')
axes[2,2].axis('off')

plt.show()
