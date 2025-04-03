import os
import json

# Carpeta de imágenes
directorio = "imagenes"

# Filtrar imágenes (png, jpg, jpeg)
imagenes = [f for f in os.listdir(directorio) if f.lower().endswith(("png", "jpg", "jpeg"))]

# Guardar lista en imagenes.json
with open("imagenes.json", "w", encoding="utf-8") as archivo_json:
    json.dump(imagenes, archivo_json, indent=4)

print("📄 imagenes.json generado con éxito ✅")
# Guardar lista en imagenes.txt