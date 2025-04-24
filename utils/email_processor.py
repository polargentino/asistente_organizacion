from transformers import pipeline

# Cargar modelos preentrenados
summarizer = pipeline("summarization")
generator = pipeline("text-generation", model="gpt-2")

def resumir_email(email_texto):
    """
    Genera un resumen del contenido del email utilizando un modelo de IA.
    """
    try:
        resumen = summarizer(email_texto, max_length=50, min_length=10, do_sample=False)
        return resumen[0]['summary_text']
    except Exception as e:
        return f"Error al resumir el email: {str(e)}"

def generar_respuesta_email(email_texto):
    """
    Genera una respuesta automática basada en el contenido del email utilizando un modelo de IA.
    """
    try:
        respuesta = generator(email_texto, max_length=50, num_return_sequences=1)
        return respuesta[0]['generated_text']
    except Exception as e:
        return f"Error al generar respuesta: {str(e)}"