# Importar openeo
import openeo

# Conexión y autenticación
connection = openeo.connect("openeo.dataspace.copernicus.eu")
connection.authenticate_oidc()

# Inicialización del cubo de datos con el área de interés y rango de tiempo
datacube = connection.load_collection(
    # Satélite a utilizar
    "SENTINEL2_L2A",
    # Zapopan y Guadalajara
    spatial_extent={"west": -103.4620,  # Coordenada oeste
    "south": 20.6008,   # Coordenada sur
    "east": -103.2225,  # Coordenada este
    "north": 20.7950},  # Coordenada norte
    temporal_extent=["2024-04-01", "2024-09-10"],
    bands=["B04", "B08"],  # Bandas: Green (B03), NIR (B08)
    max_cloud_cover=85,
)

# Selección de bandas y cálculo de reflectancias físicas
red = datacube.band("B04") * 0.0001
nir = datacube.band("B08") * 0.0001

# Cálculo del Índice de Vegetación de Diferencia Normalizada (NDVI)
ndvi = (nir - red) / (nir + red)

# Eliminación de la dimensión temporal tomando el valor medio por píxel
ndvi_composite = ndvi.mean_time()

# Descarga del resultado como archivo GeoTIFF
ndvi_composite.download("NDVI.tiff")
