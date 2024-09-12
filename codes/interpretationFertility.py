import rasterio
import matplotlib.pyplot as plt
import numpy as np

# Cargar el archivo BSI.tiff
with rasterio.open('BSI.tiff') as src:
    bsi = src.read(1)  # Leer la primera banda

# Crear una máscara para valores no válidos (si los hay)
mask = np.logical_or(np.isnan(bsi), np.isinf(bsi))

# Calcular los percentiles para el recorte
lower_percentile = np.percentile(bsi[~mask], 2)
upper_percentile = np.percentile(bsi[~mask], 98)

# Recortar y escalar los valores de BSI
bsi_clipped = np.clip(bsi, lower_percentile, upper_percentile)
bsi_scaled = (bsi_clipped - lower_percentile) / (upper_percentile - lower_percentile)

# Crear una figura
plt.figure(figsize=(12, 10))

# Visualizar el BSI usando una escala de colores personalizada
cmap = plt.cm.terrain  # Color map para visualización topográfica
im = plt.imshow(bsi_scaled, cmap=cmap, vmin=0, vmax=1)

# Configurar el título y las etiquetas de los ejes
plt.title('Índice de Esterilidad del Suelo (BSI)')
plt.xlabel('Columnas')
plt.ylabel('Filas')

# Añadir una barra de colores con etiquetas descriptivas
cbar = plt.colorbar(im)
cbar.set_label('BSI')
cbar.set_ticks([0, 0.5, 1])
cbar.set_ticklabels(['Suelo muy estéril', 'Suelo moderadamente estéril', 'Suelo fértil'])

# Ajustar la visualización
plt.tight_layout()

# Guardar la imagen 
plt.savefig('BSI_visualization.png', dpi=300, bbox_inches='tight')
