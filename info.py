import psutil
import platform
from datetime import datetime

def obtener_informacion_sistema():
    print("="*40, "Información del Sistema", "="*40)
    # Información del sistema operativo
    print(f"Sistema Operativo: {platform.system()}")
    print(f"Nombre del Nodo: {platform.node()}")
    print(f"Versión del SO: {platform.version()}")
    print(f"Arquitectura: {platform.machine()}")
    print(f"Procesador: {platform.processor()}")
    print(f"Python Version: {platform.python_version()}")

    # Información del CPU
    print("="*40, "Información del CPU", "="*40)
    print(f"Núcleos Físicos: {psutil.cpu_count(logical=False)}")
    print(f"Núcleos Totales (incluyendo lógicos): {psutil.cpu_count(logical=True)}")
    print(f"Frecuencia del CPU: {psutil.cpu_freq().current} MHz")
    print(f"Uso del CPU: {psutil.cpu_percent(interval=1)}%")

    # Información de la Memoria RAM
    print("="*40, "Información de la Memoria RAM", "="*40)
    memoria = psutil.virtual_memory()
    print(f"Memoria Total: {memoria.total / (1024 ** 3):.2f} GB")
    print(f"Memoria Disponible: {memoria.available / (1024 ** 3):.2f} GB")
    print(f"Uso de Memoria: {memoria.percent}%")

    # Información del Disco
    print("="*40, "Información del Disco", "="*40)
    disco = psutil.disk_usage('/')
    print(f"Espacio Total en Disco: {disco.total / (1024 ** 3):.2f} GB")
    print(f"Espacio Libre en Disco: {disco.free / (1024 ** 3):.2f} GB")
    print(f"Uso de Disco: {disco.percent}%")

if __name__ == "__main__":
    obtener_informacion_sistema()