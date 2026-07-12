"""Aplicacion de consola para probar la agenda telefonica.

Permite registrar, buscar y listar contactos de forma interactiva.
Ejecutar con:  python app.py
"""

from src.agenda import Agenda, ContactoInvalidoError


def mostrar_menu():
    print("\n===== AGENDA TELEFONICA =====")
    print("1. Registrar contacto")
    print("2. Buscar contacto")
    print("3. Listar contactos")
    print("0. Salir")


def registrar_contacto(agenda):
    nombre = input("Nombre: ")
    telefono = input("Telefono (10 digitos): ")
    try:
        contacto = agenda.registrar_contacto(nombre, telefono)
        print(
            "Contacto registrado: {} - {}".format(
                contacto["nombre"], contacto["telefono"]
            )
        )
    except ContactoInvalidoError as error:
        print("Error: {}".format(error))


def buscar_contacto(agenda):
    nombre = input("Nombre a buscar: ")
    contacto = agenda.buscar_contacto(nombre)
    if contacto:
        print(
            "Encontrado: {} - {}".format(
                contacto["nombre"], contacto["telefono"]
            )
        )
    else:
        print("Contacto no encontrado")


def listar_contactos(agenda):
    if agenda.total_contactos() == 0:
        print("La agenda esta vacia")
        return
    print("Contactos registrados ({}):".format(agenda.total_contactos()))
    for contacto in agenda.listar_contactos():
        print("- {}: {}".format(contacto["nombre"], contacto["telefono"]))


def main():
    agenda = Agenda()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()
        if opcion == "1":
            registrar_contacto(agenda)
        elif opcion == "2":
            buscar_contacto(agenda)
        elif opcion == "3":
            listar_contactos(agenda)
        elif opcion == "0":
            print("Saliendo de la agenda. Hasta pronto!")
            break
        else:
            print("Opcion invalida. Intente nuevamente.")


if __name__ == "__main__":
    main()
