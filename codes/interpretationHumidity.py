import rasterio
import matplotlib.pyplot as plt
import numpy as np

# Cargar el archivo NDMI.tiff
with rasterio.open('NDMI.tiff') as src:
    ndmi = src.read(1)  # Leer la primera banda

# Crear una máscara para valores no válidos (si los hay)
mask = np.logical_or(np.isnan(ndmi), np.isinf(ndmi))

# Calcular los percentiles para el recorte
lower_percentile = np.percentile(ndmi[~mask], 2)
upper_percentile = np.percentile(ndmi[~mask], 98)

# Recortar y escalar los valores de NDMI
ndmi_clipped = np.clip(ndmi, lower_percentile, upper_percentile)
ndmi_scaled = (ndmi_clipped - lower_percentile) / (upper_percentile - lower_percentile)

# Crear una figura
plt.figure(figsize=(12, 10))

# Visualizar el NDMI usando una escala de colores personalizada
cmap = plt.cm.RdYlBu  # Red-Yellow-Blue colormap
im = plt.imshow(ndmi_scaled, cmap=cmap, vmin=0, vmax=1)

# Configurar el título y las etiquetas de los ejes
plt.title('Índice de Diferencia Normalizada de Humedad (NDMI)')
plt.xlabel('Columnas')
plt.ylabel('Filas')

# Añadir una barra de colores con etiquetas descriptivas
cbar = plt.colorbar(im)
cbar.set_label('NDMI')
cbar.set_ticks([0, 0.5, 1])
cbar.set_ticklabels(['Baja humedad', 'Humedad moderada', 'Alta humedad'])

# Ajustar la visualización
plt.tight_layout()

# Guardar la imagen
plt.savefig('NDMI_visualization.png', dpi=300, bbox_inches='tight')