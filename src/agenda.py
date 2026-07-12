"""Agenda telefonica: registro y busqueda de contactos."""

from src.validaciones import validar_nombre, validar_telefono


class ContactoInvalidoError(ValueError):
    """Se lanza cuando el nombre o el telefono no cumplen las reglas."""


class Agenda:
    """Agenda telefonica en memoria."""

    def __init__(self):
        # Clave: nombre en minusculas. Valor: dict del contacto.
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

    def listar_contactos(self):
        """Devuelve la lista de todos los contactos registrados."""
        return list(self._contactos.values())

    def total_contactos(self):
        """Cantidad de contactos registrados."""
        return len(self._contactos)
