from utils.file_organizer import organizar_archivos
from utils.email_processor import resumir_email, generar_respuesta_email
from utils.calendar_manager import programar_reunion
from utils.summarizer import resumir_documento

def menu_principal():
    print("=== Asistente de Productividad ===")
    print("1. Organizar archivos automáticamente")
    print("2. Resumir un documento o artículo")
    print("3. Generar respuesta automática para un email")
    print("4. Programar una reunión analizando disponibilidad")
    print("5. Salir")
    opcion = input("Selecciona una opción: ")
    return opcion

def main():
    while True:
        opcion = menu_principal()

        if opcion == "1":
            organizar_archivos()
        elif opcion == "2":
            ruta_documento = input("Ingresa la ruta del documento: ")
            resumen = resumir_documento(ruta_documento)
            print("Resumen:", resumen)
        elif opcion == "3":
            email_texto = input("Pega el contenido del email: ")
            respuesta = generar_respuesta_email(email_texto)
            print("Respuesta generada:", respuesta)
        elif opcion == "4":
            programar_reunion()
        elif opcion == "5":
            print("Saliendo del asistente...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()