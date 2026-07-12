from src.agenda import Agenda


def ejecutar_flujo():
    print("Bienvenido a la agenda telefonica")
    agenda = Agenda()

    agenda.registrar_contacto("Juan Perez", "0991234567")
    print("Contacto registrado: Juan Perez - 0991234567")

    contacto = agenda.buscar_contacto("Juan Perez")
    print(f"Contacto encontrado: {contacto['nombre']} - {contacto['telefono']}")

    print("Final de la ejecucion del flujo")


if __name__ == "__main__":
    ejecutar_flujo()
