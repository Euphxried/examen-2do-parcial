import os
from asistente import AsistenteAcademico

class MenuPrincipal:
    def __init__(self):
        self.opcion = "0"
        self.asistente = AsistenteAcademico()

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def pausar(self):
        input("\nPresione Enter para continuar...")

    def mostrar_menu(self):
        print("--------- Menú Principal ---------")
        print("1. Tutor de Programación")
        print("2. Tutor de Inteligencia Artificial")
        print("3. Tutor de Bases de datos")

        print("0. Salir")

    def ejecutar_opcion(self):
        while True:
            self.limpiar_pantalla()
            self.mostrar_menu()
            self.opcion = input("Seleccione una opción: ")

            if self.opcion in ["1", "2", "3"]:
                self.asistente.iniciar_chat(self.opcion)
            elif self.opcion == "0":
                print("Saliendo del programa...")
                break

            else:
                print("Opción inválida, seleccione otra")
            self.pausar()

if __name__ == "__main__":
    menu = MenuPrincipal()
    menu.ejecutar_opcion()