# Importar librerias
import rasterio
import matplotlib.pyplot as plt
import numpy as np


# Cargar el archivo NDVI.tiff
with rasterio.open('NDVI.tiff') as src:
    ndvi = src.read(1)  # Leer la primera banda

# Crear una máscara para valores no válidos (si los hay)
mask = np.logical_or(np.isnan(ndvi), np.isinf(ndvi))

# Calcular los percentiles para el recorte
lower_percentile = np.percentile(ndvi[~mask], 2)
upper_percentile = np.percentile(ndvi[~mask], 98)

# Recortar y escalar los valores de NDVI
ndvi_clipped = np.clip(ndvi, lower_percentile, upper_percentile)
ndvi_scaled = (ndvi_clipped - lower_percentile) / (upper_percentile - lower_percentile)

# Crear una figura
plt.figure(figsize=(12, 10))

# Visualizar el NDVI usando una escala de colores personalizada
cmap = plt.cm.RdYlGn  # Red-Yellow-Green colormap
im = plt.imshow(ndvi_scaled, cmap=cmap, vmin=0, vmax=1)

# Configurar el título y las etiquetas de los ejes
plt.title('Índice de Vegetación de Diferencia Normalizada (NDVI)')
plt.xlabel('Columnas')
plt.ylabel('Filas')

# Añadir una barra de colores con etiquetas descriptivas
cbar = plt.colorbar(im)
cbar.set_label('NDVI')
cbar.set_ticks([0, 0.5, 1])
cbar.set_ticklabels(['Baja vegetación', 'Vegetación moderada', 'Alta vegetación'])

# Ajustar la visualización
plt.tight_layout()

# Guardar la imagen
plt.savefig('NDVI_visualization.png', dpi=300, bbox_inches='tight')
