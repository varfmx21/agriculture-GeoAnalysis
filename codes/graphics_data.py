import matplotlib.pyplot as plt
import numpy as np

def leer_datos(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.readlines()

    # Inicializar variables
    temperaturas_max = []
    temperaturas_min = []
    temperaturas_med = []
    precipitacion = []

    meses = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]

    seccion_actual = ""
    
    for linea in contenido:
        linea = linea.strip()

        # Detección de secciones
        if "TEMPERATURA MÁXIMA" in linea:
            seccion_actual = "temperatura_maxima"
        elif "TEMPERATURA MÍNIMA" in linea:
            seccion_actual = "temperatura_minima"
        elif "TEMPERATURA MEDIA" in linea:
            seccion_actual = "temperatura_media"
        elif "PRECIPITACIÓN" in linea:
            seccion_actual = "precipitacion"

        # Extraer datos según la sección y recortar a los primeros 12 meses
        if seccion_actual == "temperatura_maxima" and "NORMAL" in linea:
            temperaturas_max = [float(x) for x in linea.split()[1:13]]
        elif seccion_actual == "temperatura_minima" and "NORMAL" in linea:
            temperaturas_min = [float(x) for x in linea.split()[1:13]]
        elif seccion_actual == "temperatura_media" and "NORMAL" in linea:
            temperaturas_med = [float(x) for x in linea.split()[1:13]]
        elif seccion_actual == "precipitacion" and "NORMAL" in linea:
            precipitacion = [float(x) for x in linea.split()[1:13]]

    return meses, temperaturas_max, temperaturas_min, temperaturas_med, precipitacion

# Graficar los datos
def graficar_datos(meses, temperaturas_max, temperaturas_min, temperaturas_med, precipitacion):
    # Configuración de subplots
    fig, axs = plt.subplots(2, 1, figsize=(10, 12))

    # Gráfico de temperaturas
    axs[0].plot(meses, temperaturas_max, label="Temperatura Máxima", color='red', marker='o')
    axs[0].plot(meses, temperaturas_min, label="Temperatura Mínima", color='blue', marker='o')
    axs[0].plot(meses, temperaturas_med, label="Temperatura Media", color='green', marker='o')
    axs[0].set_title("Temperaturas Normales (1991-2020)")
    axs[0].set_xlabel("Meses")
    axs[0].set_ylabel("Temperatura (°C)")
    axs[0].legend()
    axs[0].grid(True)

    # Gráfico de precipitación
    axs[1].bar(meses, precipitacion, color='skyblue')
    axs[1].set_title("Precipitación Normal (1991-2020)")
    axs[1].set_xlabel("Meses")
    axs[1].set_ylabel("Precipitación (mm)")
    axs[1].grid(True)

    # Mostrar gráficos
    plt.tight_layout()
    plt.show()

# Archivo de datos
archivo = 'D:/workspace/Agro-DataThon/agriculture-GeoAnalysis/data/data_comisionNacionalDelAgua_Zapopan.txt'

# Leer los datos y graficarlos
meses, temperaturas_max, temperaturas_min, temperaturas_med, precipitacion = leer_datos(archivo)
graficar_datos(meses, temperaturas_max, temperaturas_min, temperaturas_med, precipitacion)
