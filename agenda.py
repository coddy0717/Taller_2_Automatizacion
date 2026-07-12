"""Agenda telefonica.

Permite registrar y consultar contactos aplicando dos reglas de negocio:

* El nombre debe estar compuesto unicamente por texto (letras y espacios).
* El numero telefonico debe tener exactamente 10 digitos.

Modulo desarrollado para el Taller Grupal 2 - Integracion Continua con
GitHub Actions (Maestria en Ingenieria en Software).
"""

import re

# Nombre: solo letras (incluye vocales acentuadas y la enie) y espacios.
_PATRON_NOMBRE = re.compile(r"^[A-Za-zAEIOUaeiouNnÀ-ſ\s]+$")

# Telefono: exactamente 10 digitos.
_PATRON_TELEFONO = re.compile(r"^\d{10}$")


class ContactoInvalidoError(ValueError):
    """Se lanza cuando el nombre o el telefono no cumplen las reglas."""


def validar_nombre(nombre):
    """Valida que ``nombre`` sea texto (letras y espacios), no vacio.

    Devuelve ``True`` si es valido; en caso contrario devuelve ``False``.
    """
    if not isinstance(nombre, str):
        return False
    nombre = nombre.strip()
    if not nombre:
        return False
    return bool(_PATRON_NOMBRE.match(nombre))


def validar_telefono(telefono):
    """Valida que ``telefono`` tenga exactamente 10 digitos.

    Acepta ``str`` o ``int``. Devuelve ``True`` o ``False``.
    """
    if isinstance(telefono, int) and not isinstance(telefono, bool):
        telefono = str(telefono)
    if not isinstance(telefono, str):
        return False
    return bool(_PATRON_TELEFONO.match(telefono.strip()))


class Agenda:
    """Agenda telefonica en memoria."""

    def __init__(self):
        # Clave: nombre normalizado en minusculas. Valor: dict del contacto.
        self._contactos = {}

    # ------------------------------------------------------------------
    # Desarrollador A: registro de contactos + validaciones
    # ------------------------------------------------------------------
    def registrar_contacto(self, nombre, telefono):
        """Registra un contacto tras validar nombre y telefono.

        Lanza :class:`ContactoInvalidoError` si algun dato es invalido o si
        el contacto ya existe.
        """
        if not validar_nombre(nombre):
            raise ContactoInvalidoError(
                "El nombre debe contener unicamente texto (letras y espacios)."
            )
        if not validar_telefono(telefono):
            raise ContactoInvalidoError(
                "El telefono debe tener exactamente 10 digitos."
            )

        nombre = nombre.strip()
        telefono = str(telefono).strip()
        clave = nombre.lower()

        if clave in self._contactos:
            raise ContactoInvalidoError(
                "El contacto '{}' ya existe en la agenda.".format(nombre)
            )

        contacto = {"nombre": nombre, "telefono": telefono}
        self._contactos[clave] = contacto
        return contacto

    # ------------------------------------------------------------------
    # Desarrollador B: busqueda de contactos
    # ------------------------------------------------------------------
    def buscar_contacto(self, nombre):
        """Busca un contacto por nombre exacto (sin distinguir mayusculas).

        Devuelve el diccionario del contacto o ``None`` si no existe.
        """
        if not isinstance(nombre, str):
            return None
        return self._contactos.get(nombre.strip().lower())

    def buscar_por_coincidencia(self, texto):
        """Devuelve la lista de contactos cuyo nombre contiene ``texto``."""
        if not isinstance(texto, str) or not texto.strip():
            return []
        texto = texto.strip().lower()
        return [
            contacto
            for clave, contacto in self._contactos.items()
            if texto in clave
        ]

    def total_contactos(self):
        """Cantidad de contactos registrados."""
        return len(self._contactos)
