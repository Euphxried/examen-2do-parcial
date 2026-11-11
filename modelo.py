from langchain_ollama import ChatOllama

class ModeloIA:
    def __init__(self):
        self.modelo = ChatOllama(model="qwen2.5:3b", temperature=0.1)

    def obtener_system_message(self, opcion):
        prompts = {
            "1": "Eres un tutor universitario experto en Programación responde en español, usa lenguaje sencillo, explica paso a paso e incluye ejemplos en Python",
            "2": "Eres un tutor universitario experto en Inteligencia Artificial responde en español, usa lenguaje sencillo, explica claramente e incluye ejemplos cuando convenga",
            "3": "Eres un tutor universitario experto en Bases de Datos responde en español, usa lenguaje sencillo, enfócate en conceptos relacionales y SQL"
        }
        return prompts[opcion]

    def generar_respuesta(self, prompt):
        respuesta = self.modelo.invoke(prompt)
        return respuesta