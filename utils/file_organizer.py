import os
import shutil

def organizar_archivos(directorio="~/Downloads"):
    directorio = os.path.expanduser(directorio)
    for archivo in os.listdir(directorio):
        ruta_completa = os.path.join(directorio, archivo)
        if os.path.isfile(ruta_completa):
            extension = archivo.split('.')[-1].lower()
            carpeta_destino = os.path.join(directorio, extension)
            os.makedirs(carpeta_destino, exist_ok=True)
            shutil.move(ruta_completa, os.path.join(carpeta_destino, archivo))
    print("Archivos organizados exitosamente.")