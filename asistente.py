import json
import os
from pathlib import Path
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, message_to_dict, messages_from_dict
from modelo import ModeloIA

class AsistenteAcademico:
    def __init__(self):
        self.modelo_ia = ModeloIA()
        self.archivo = Path(__file__).parent / "historial.json"
        self.historial = []

    def cargar_historial(self):
        if self.archivo.exists():
            with open(self.archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
                self.historial = messages_from_dict(datos)
                self.historial[0] = self.system_message

    def guardar_historial(self):
        datos = [message_to_dict(m) for m in self.historial]
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)

    def iniciar_chat(self, opcion):
        prompt_sistema = self.modelo_ia.obtener_system_message(opcion)
        self.system_message = SystemMessage(content=prompt_sistema)
        
        self.historial = [self.system_message]
        self.cargar_historial()

        while True:
            pregunta = input("\nUsuario: ")
            
            if pregunta.lower() == "salir":
                break
                
            if pregunta.lower() == "nuevo":
                self.historial = [self.system_message]
                self.guardar_historial()
                os.system('cls')
                print("Se inició una nueva conversación, el historial anterior fue borrado")
                continue
                
            if pregunta.lower() == "historial":
                print(f"\n{"-"*30} Historial de conversación {"-"*30}")
                for m in self.historial:
                    if isinstance(m, HumanMessage):
                        print(f"Usuario: {m.content}")
                    elif isinstance(m, AIMessage):
                        print(f"IA: {m.content}")
                continue

            self.historial.append(HumanMessage(content=pregunta))
            respuesta = self.modelo_ia.generar_respuesta(self.historial)

            print("IA:", respuesta.content)
            self.historial.append(respuesta)
            self.guardar_historial()