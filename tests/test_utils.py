import unittest
from utils.file_organizer import organizar_archivos
from utils.email_processor import resumir_email, generar_respuesta_email
from utils.calendar_manager import programar_reunion
from utils.summarizer import resumir_documento

class TestUtils(unittest.TestCase):
    def test_resumir_email(self):
        """
        Prueba que el resumen del email sea una cadena válida.
        """
        email = "Este es un email de prueba para verificar el resumen."
        resumen = resumir_email(email)
        self.assertIsInstance(resumen, str)  # Verifica que el resumen sea una cadena
        self.assertGreater(len(resumen), 0)  # Verifica que el resumen no esté vacío

    def test_generar_respuesta_email(self):
        """
        Prueba que la respuesta generada sea una cadena válida.
        """
        email = "Hola, ¿cómo estás?"
        respuesta = generar_respuesta_email(email)
        self.assertIsInstance(respuesta, str)  # Verifica que la respuesta sea una cadena
        self.assertGreater(len(respuesta), 0)  # Verifica que la respuesta no esté vacía

    def test_programar_reunion(self):
        """
        Prueba que la función de programar reunión no genere errores.
        """
        try:
            programar_reunion()
            resultado = True
        except Exception as e:
            print(f"Error: {e}")
            resultado = False
        self.assertTrue(resultado)

    def test_resumir_documento(self):
        """
        Prueba que el resumen del documento sea una cadena válida.
        """
        texto = "Este es un documento largo que necesita ser resumido."
        resumen = resumir_documento(texto)
        self.assertIsInstance(resumen, str)  # Verifica que el resumen sea una cadena
        self.assertGreater(len(resumen), 0)  # Verifica que el resumen no esté vacío

if __name__ == "__main__":
    unittest.main()