from transformers import pipeline

# Cargar un modelo preentrenado para resumen
summarizer = pipeline("summarization")

def resumir_documento(texto):
    resumen = summarizer(texto, max_length=150, min_length=30, do_sample=False)
    return resumen[0]['summary_text']