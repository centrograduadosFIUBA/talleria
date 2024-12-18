import openai
from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv(find_dotenv())

# Configura tu clave de API de OpenAI
try:
    cliente = OpenAI(api_key = os.environ.get('OPENAI_API_KEY'))
except openai.OpenAIError as e:
    print(f"Error al configurar la API de OpenAI: {e}")    

# Función para generar una respuesta usando la API de OpenAI
def generar_respuesta(pregunta):
    try:
        # Solicita una respuesta al modelo
        respuesta = cliente.chat.completions.create(
            model="gpt-4o-mini",  # Usa el modelo más reciente
            messages=[
                {"role": "system", "content": "Eres un asistente útil y amigable."},
                {"role": "user", "content": pregunta}
            ],
            max_tokens=100,  # Maximo de palabras
            temperature=0.7  # Ajusta la creatividad de las respuestas
        )
        return respuesta.choices[0].message.content.strip()
    except openai.APIError as e:
    #Handle API error here
        print(f"OpenAI API devolvio un error: {e}")
        pass
    except openai.APIConnectionError as e:
    #Handle connection error here
        print(f"Fallo al conectar con OpenAI API: {e}")
        pass

# Función principal
def main():
    print("Bienvenido al Chatbot de OpenAI")

    while True:
        pregunta = input("Escribe tu pregunta (o 'salir' para finalizar): ")
        
        if pregunta.lower() == 'salir':
            print("¡Hasta luego!")
            break
        
        respuesta = generar_respuesta(pregunta)
        print("Agente-Bot:", respuesta)

# Punto de entrada del programa
if __name__ == "__main__":
    main()