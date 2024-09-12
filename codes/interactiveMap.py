import folium
from folium.raster_layers import ImageOverlay
from PIL import Image
import base64
from io import BytesIO

# Función para cargar imágenes PNG generadas como base64
def load_png_as_base64(image_path):
    with Image.open(image_path) as img:
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
        return f"data:image/png;base64,{img_base64}"

# Cargar las imágenes PNG generadas por Matplotlib como base64
ndvi_img = load_png_as_base64("NDVI_Interactive.png")
ndmi_img = load_png_as_base64("NDMI_Interactive.png")
bsi_img = load_png_as_base64("BSI_Interactive.png")

# Definir los límites manualmente para cada imagen
latlon_bounds = [[20.6008, -103.4620], [20.7950, -103.2225]]

# Crear mapa base centrado en el área de interés
m = folium.Map(location=[20.7, -103.34], zoom_start=11)

# Agregar las imágenes como capas al mapa
folium.raster_layers.ImageOverlay(
    image=ndvi_img,
    bounds=latlon_bounds,
    opacity=0.6,
    name='NDVI'
).add_to(m)

folium.raster_layers.ImageOverlay(
    image=ndmi_img,
    bounds=latlon_bounds,
    opacity=0.6,
    name='NDMI'
).add_to(m)

folium.raster_layers.ImageOverlay(
    image=bsi_img,
    bounds=latlon_bounds,
    opacity=0.6,
    name='BSI'
).add_to(m)

# Ajustar el mapa para que se limite a las coordenadas especificadas
m.fit_bounds(latlon_bounds)

# Añadir el control de capas
folium.LayerControl(collapsed=False).add_to(m)

# Guardar el mapa como archivo HTML
map_path = 'mapa_interactivo_con_imagenes.html'
m.save(map_path)

