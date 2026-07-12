"""Validaciones de los datos de un contacto.

Reglas de negocio del Taller Grupal 2:

* El nombre debe estar compuesto unicamente por texto (letras y espacios).
* El numero telefonico debe tener exactamente 10 digitos.
"""

import re

# Nombre: solo letras (incluye vocales acentuadas y la enie) y espacios.
_PATRON_NOMBRE = re.compile(r"^[A-Za-zAEIOUaeiouNnÀ-ſ\s]+$")

# Telefono: exactamente 10 digitos.
_PATRON_TELEFONO = re.compile(r"^\d{10}$")


def validar_nombre(nombre):
    """Valida que ``nombre`` sea texto (letras y espacios) y no este vacio."""
    if not isinstance(nombre, str):
        return False
    nombre = nombre.strip()
    if not nombre:
        return False
    return bool(_PATRON_NOMBRE.match(nombre))


def validar_telefono(telefono):
    """Valida que ``telefono`` tenga exactamente 10 digitos.

    Acepta ``str`` o ``int``.
    """
    if isinstance(telefono, int) and not isinstance(telefono, bool):
        telefono = str(telefono)
    if not isinstance(telefono, str):
        return False
    return bool(_PATRON_TELEFONO.match(telefono.strip()))
