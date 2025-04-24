from datetime import datetime, timedelta

def programar_reunion():
    # Simulación de análisis de disponibilidad
    ahora = datetime.now()
    sugerencia = ahora + timedelta(hours=1)
    print(f"Reunión sugerida para: {sugerencia.strftime('%Y-%m-%d %H:%M')}")